import Buried_Water_Potentials as BWP
import urllib
import os

for line in open('pdb_list_example.txt'):
    #argument is the file for the list of all PDB files to analyze
    try:
        line = str(line).strip()
        print "Working on", line
        urllib.urlretrieve('http://www.rcsb.org/pdb/files/%s.pdb' % line, '%s.pdb' % line)
        PdbFile = '%s.pdb' % line
        BWP.f(PdbFile)
    	print "Finished analysis without error :)"
        os.remove(PdbFile)
    except IndexError:
        #some PDB files give an Index Error, so we will just ignore them
        errorstring = "file " + line + " has index error"
        os.remove(PdbFile)
        print(errorstring)