# buried-water-electrostatics

We examined the electrostatic potential at the locations of buried waters within proteins to see if this exhibited any asymmetric behavior (previous work we had done suggested perhaps it might) and found none. Here's the code to reproduce.

The file `Buried_Water_Potentials.py` is a python module containing the function "`f`" which takes a PDB file as input, and uses OpenEye Scientific modules (`oechem`, `oeszmap`, `oegrid`, `oequacpac`, and `oezap`) to analyse the electrostatics around each buried water in the protein file.

`Buried_Water_Run_Example_Script.py` is a python script that will run through the `master_pdb_list.txt`, extract the four-letter PDB code from each line, download the corresponding file from the Protein Data Bank, run the `Buried_Water_Potentials` module on it (which will output a file containing analysis information, or output an error), and delete the PDB file, before moving on to the next.

WARNING: `master_pdb_list.txt` contains the four-letter codes for ~12k PDB files. This master list may need to be split in to smaller lists, to split computation time in to more manageable segments, but the underlying work flow will be identitcal (the `Buried_Water_Run_Example_Script.py` can be run on a list of any length, provided that it contains one column of four-letter PDB codes). 

The `master_pdb_list.txt` PDB codes were culled from the Dunbrack PISCES Protein Sequence Culling Server: http://dunbrack.fccc.edu/PISCES.php with the following stipulations: 
- Maximum Percentage Identity - 25; 
- Minimum Resolution - 0.0; 
- Maximum Resolution - 3.0; 
- Maximum R-Value - 0.3; 
- Minimum Chain Length - 40; 
- Maximum Chain Length - 10000; 
- skipped non-X-ray and CA-only entries; 
- culled pdbs by chain, not entry. 

This specification will result in a list of PDBs fulfill these requirements, but will contain multiple entries for different chains in the same PDB file. To produce the `master_pdb_list.txt`, the four letter codes were stripped from the list produced by the PISCES Server, and written to a 1-column text file, and multiple entreis from the same protein were deleted, leaving only one entry from each protein.

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

And the ...Example_Script,py will terminate. These proteins do not have .pdb formatted files to download on the PDB database, thus the url-retrieval for them fails. The Buried_Water_Run_Example_Script.py script will output an error for the analysis of these files and terminate.
