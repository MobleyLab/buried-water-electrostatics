# buried-water-electrostatics

We examined the electrostatic potential at the locations of buried waters within proteins to see if this exhibited any asymmetric behavior (previous work we had done suggested perhaps it might) and found none. Here's the code to reproduce.

The file Buried_Water_Potentials.py is a python module containing the function "f" which takes a PDB file as input, and uses OpenEye software to analyse the electrostatics around each buried water in the file.

Buried_Water_Run_Example_Script.py is a python script that will run through the master_pdb_list.txt, extract the four-letter PDB code from each line, download the corresponding code from the Protein Data Bank, run the Buried_Water_Potentials module on it, output a file containing analysis information (or output an error), and delete the PDB file, before moving on to the next.

WARNING: master_pdb_list.txt contains the codes for ~12k PDB files. This master list may need to be split in to smaller lists, to split computation time in to more manageable segments, but the underlying work flow will be identitcal (the Buried_Water_Run_Example_Script.py can be run on a list of any length, provided that it contains one column of four-letter PDB codes). 
