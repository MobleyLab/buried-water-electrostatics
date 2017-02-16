#!/usr/bin/env python
import sys
from openeye.oechem import *
from openeye.oeszmap import *
from openeye.oegrid import *
from openeye.oequacpac import *
from openeye.oezap import *

def OutputPotentialData ( file ):
    
    # Parameters
    # ------

    #   file: name of PDB file to be analyzed
    #   i.e. "{four_letter_code}.pdb"

    # Returns
    # ------

    #    7-column data file containing the
    #    index and x, y, and z, coordinates
    #    of each water molecule, the Burial
    #    Coefficient -- 0, unburied, to
    #    1, buried -- the Electric Potential
    #    (in kcal/mole), and the B-factor

    #    (n.b. output data file contains
    #    a header)    

    # Extracting the PDB code from the input file
    # and setting the output file name
    filename = file[:-4]
    out_filename = filename + '_wat_info.dat'

    # Defining the input variable
    ifs = oemolistream()

    # Checking to make sure that the input files
    # inputted as arguments are readable by the
    # the OpenEye modules
    """
        WARNING: .open() will open any file, and
        return "True", even if the argument
        is a non-molecule file, like a text file, as
        long as the file is in the directory, so 
        this trip-wire is not bullet-proof.
        It will to the ouput line:
        > "Warning: Unknown file format set in input stream."
        but the rest of the code will still run

        The second of two ifs test to see if the format
        of the input file is "_.pdb", but this can be tweaked
        if other file formats are required
    """
    if not ifs.open( file ):
        OEThrow.Fatal("Cannot open %s" % argv[1])
    if not ifs.GetFormat() == 3:
        OEThrow.Fatal("%s in wrong format. Must be '.pdb'" % argv[1])

    # Setting up the protein, water, ligand
    # and other molecules as OEGraphMols 
    # and reading them in
    # If OEReadMolecule is unable to read the
    # PDB file, the script will terminate
    fullmol = OEGraphMol()
    if not OEReadMolecule(ifs, fullmol):
        OEThrow.Fatal("Unable to read %s." % file)

    # Setting up the segment molecules
    prot = OEGraphMol()
    lig = OEGraphMol()
    wat = OEGraphMol()
    other = OEGraphMol()

    # Splitting the full molecule in to
    # constituent segment molecules
    OESplitMolComplex(lig, prot, wat, other, fullmol)
    
    # Preparing the segments
    # Protein
    OEPlaceHydrogens(prot)
    OEAssignBondiVdWRadii(prot)
    OEMMFFAtomTypes(prot)
    OEMMFF94PartialCharges(prot)

    # Water
    OEAssignBondiVdWRadii(wat)
    OEMMFFAtomTypes(wat)
    OEMMFF94PartialCharges(wat)

    # Ligand
    OEAssignBondiVdWRadii(lig)
    OEMMFFAtomTypes(lig)
    OEMMFF94PartialCharges(lig)

    # Others
    OEAssignBondiVdWRadii(other)
    OEMMFFAtomTypes(other)
    OEMMFF94PartialCharges(other)

    # Starting up the Szmap engine (vroom vroom)
    opt = OESzmapEngineOptions()
    sz = OESzmapEngine(prot, opt)
    epsin = 1.0
    zap = OEZap()
    zap.SetInnerDielectric(epsin)
    zap.SetMolecule(prot)

    # Data Output
    '''
        Loops below output the index number, coordinates,
        Burial Coefficient, Potential Energy, and B-factor
        for each water identified in the input molecule,
        and output this information line by line to the
        output file, named: "{PDB_code}_wat_info.dat"
    '''
    coords = OEFloatArray(3)
    grid = OEScalarGrid()
    if zap.CalcPotentialGrid(grid):
        # Creating the output data file
        with open(out_filename, 'w') as f:
            f.write("num, x, y, z, Burial_Coef., Potential_Energy, B_factor \n")
            for atom in wat.GetAtoms():
                if OEGetResidueIndex(atom)==OEResidueIndex_HOH:
                    res = OEAtomGetResidue(atom)
                    wat.GetCoords(atom, coords)
                    f.write(
                        "%g %.5f %.5f %.5f %.5f %.5f %.3f\n" \
                        % (atom.GetIdx(), coords[0], coords[1], coords[2], 
                            OECalcSzmapValue(sz, coords, OEEnsemble_ProbeBurial),
                            grid.GetValue(coords[0], coords[1], coords[2]),
                            res.GetBFactor()
                            ))
            for atom in other.GetAtoms():
                if OEGetResidueIndex(atom)==OEResidueIndex_HOH:
                    res = OEAtomGetResidue(atom)
                    other.GetCoords(atom, coords)
                    f.write(
                        "%g %.5f %.5f %.5f %.5f %.5f %.3f\n" \
                        % (atom.GetIdx(), coords[0], coords[1], coords[2], 
                            OECalcSzmapValue(sz, coords, OEEnsemble_ProbeBurial),
                            grid.GetValue(coords[0], coords[1], coords[2]),
                            res.GetBFactor()
                            ))
