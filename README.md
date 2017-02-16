# buried-water-electrostatics

Motivation and Goal
-------------------

We examined the electrostatic potential at the locations of buried waters within proteins to see if this exhibited any asymmetric behavior -- [previous work we had done](http://pubs.acs.org/doi/abs/10.1021/jp709958f) (Mobley et al. 2008, J. Phys. Chem) suggested perhaps it migh -- and found none. 

We built a list of ~12,000 high-resolution PDB files (criterea and culling method laid out below), examined the electrostatic potential at the position of each of the buried waters in every file, and plotted the results in a histogram (which is shown in the file `Elec_Pot_Hist_b_fac_25.png`).

In this repository is all of the code to reproduce, the data produced by our analysis, and the plot of the data produced.

Methods
-------

The file `Buried_Water_Potentials.py` is a python module containing the function "`OutputPotentialData`" which takes a PDB file as input, and uses OpenEye Scientific toolkits version 2017.2b3 (`oechem`, `oeszmap`, `oegrid`, `oequacpac`, and `oezap` modules) to analyse the electrostatics around each buried water in the protein file, outputting the Burial Coefficient (a measure of how buried the water is in the protein -- 1 for fully buried, 0 for not buried at all), the Potential Energy (in kcal/mole), and the B factor (temperature factor, a measure of the thermal fluctuation of the water during crystallography). (N.B. the version of OpenEye Software with which this script was written only works with python version 2.7)

`Buried_Water_Run_Example_Script.py` is a python script that will run through the `master_pdb_list.txt` (a one-column list of 4-letter PDB codes), extract the four-letter PDB code from each line, download the corresponding file from the Protein Data Bank, run the `Buried_Water_Potentials`  module `f` function on it (which will output a file containing analysis information, or output an error, if there is a problem reading the file), and delete the PDB file, before moving on to the next.

__WARNING__: `master_pdb_list.txt` contains the four-letter codes for ~12k PDB files. This master list may need to be split in to smaller lists, to split computation time in to more reasonable segments, but the underlying work flow will be identitcal (the `Buried_Water_Run_Example_Script.py` can be run on a list of any length, provided that it contains one column of four-letter PDB codes). 

The `master_pdb_list.txt` PDB codes were culled from the Dunbrack PISCES Protein Sequence Culling Server: http://dunbrack.fccc.edu/PISCES.php with the following requirements: 
- Maximum Percentage Identity - 25; 
- Minimum Resolution - 0.0; 
- Maximum Resolution - 3.0; 
- Maximum R-Value - 0.3; 
- Minimum Chain Length - 40; 
- Maximum Chain Length - 10000; 
- skipped non-X-ray and CA-only entries; 
- culled pdbs by chain, not entry. 

This specification will result in a list of PDBs fulfill these requirements, but will contain multiple entries for different chains in the same PDB file. To produce the `master_pdb_list.txt`, the four letter codes were stripped from the list produced by the PISCES Server, and written to a 1-column text file, and multiple entries from the same protein were deleted, leaving only one entry from each protein (unique 4-letter PDB code).

Some of the proteins culled by this server have entries in the Protein Data Bank, but have atom serial numbers that are too big for the PDB format (.pdb) (100k+ atom serial numbers are unsupported - http://www.bmsc.washington.edu/CrystaLinks/man/pdb/part_62.html). You will notice that the url-retrieval for these files will result produce a "{}.pdb" file containing the following html script:

```
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
  <head>
    <title>404 Not Found</title>
  </head>
  <body>
    <h1>Not Found</h1>
    <p>The requested URL was not found on this server.</p>
    <hr>
    <address>RCSB PDB</address>
  </body>
</html>
```

and the ...Example_Script,py will terminate. These proteins do not have .pdb formatted files to download on the PDB database, thus the url-retrieval for them fails. The Buried_Water_Run_Example_Script.py script will output an error for the analysis of these files, and terminate.

`buried_wats.slurm` is an example of a script to run the analysis on a computing cluster. It will run the `Buried_Water_Run_Example_Script.py` on the `pdb_master_list.txt` and print the console output to `buried_wats_logfile.log`. The file `buried_water_data_v1.dat` is three-column data file containing the aggregate of all of the Potential, Buried, and B-factor data produced by our analysis (~2.5 million individual waters analyzed).

The file `plotting_elec_pot_data.py` is a script which reads in `buried_water_data_v1.dat`, picks out only the waters with B-factors less than 25, and plots a hisogram of all of the data (fitted with a gaussian), and a separate histogram containing only the data from waters with B-factors less than 25 (also fitted with a gaussian). It also prints to the console the information from the fit, including the Mean, Standard Deviation, and the Standard Error. Plotting, fitting, and analysis is done with `matplotlib.pyplot`, `scipy.curve_fit` and `numpy` python modules. An example of the plot produced by this analysis is also included: `Elec_Pot_Hist_b_fac_25.png`.

The file `DWCode.py` is a helpful module used to make readin in, and writing out, of data for plotting and analysis easier.

Also included is an example of a script (`Buried_Wat_Beta_PDB_Generator.py`) which will use a similar protocol to `Buried_Water_Potentials.py` to analyze a pdb file, and output a "fake" pdb file containing particles at the positions of the buried waters of the input pdb file, with beta factors corresponding to their burial coefficients. This is a useful sanity checking script for the analysis of the buried waters (in VMD, coloring by Beta factor, the buried waters should appear in blue, moving through white for slightly buried waters, and red for unburied waters). It is run as follows:

`> python Buried_Wat_Beta_PDB_Generator.py {4-letter-PDB-code}.pdb`

and outputs a file named `{4-letter-PDB-code}_wats_burial_beta.pdb`. This often takes quite a while to complete for large PDB files. It can be loaded along with the pdb file used to create the "fake" pdb file to verify that the software is working correctly.

## Authors and contributors

This is a project which was originally begun by Hanna Liao, an undergraduate in the Mobley lab, after a suggestion from an audience member during a talk some years ago on water asymmetry. It went unfinished until David Wych rotated in the Mobley lab in Winter 2017; he was able to finish off this work.

We are also particularly grateful to James Haigh of OpenEye Scientific Software, on the support team, for his help with aspects of this project such as on how to calculate water burial coefficients.

If this were a paper, the authors list would read this way, presumably:
- David Wych (UCI)
- Hanna Liao (UC Berkeley)
- James Haigh (OpenEye)
- David L. Mobley (UCI)
