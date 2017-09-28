import csv
import itertools
import sys

# open_file reads tab delimited files
# to read space delimited, simply change
# the line that has "file = csv.reader...."
# delimiter arg to:
# delimiter = ' '

def open_file( f_inp, delim=' ' ):
    with open( f_inp, 'r' ) as csv_file:
        if delim == '\t':
            file = csv.reader( csv_file , delimiter='\t')
        elif delim == ' ':
            file = csv.reader( csv_file , delimiter=' ')
        try:
            file.__next__(); file.__next__()
        except StopIteration:
            # print("File has no data!")
            raise
        csv_file.seek(0)
        has_header = csv.Sniffer().has_header(f_inp)
        if has_header:
            file.__next__()
        col_1, col_2 = itertools.tee(file)
        del col_1
        x=[];y=[];z=[];u=[];v=[]; w=[]; p=[];
        data = list(col_2)
        if len(data[0]) == 1:
            for i in range(len(data)):
                x.append(float(data[i][0]))
            return x
            print("Created 1 variable...")
        if len(data[0]) == 2:
            for i in range(len(data)):
                    x.append(float(data[i][0]))
                    y.append(float(data[i][1]))
            return x, y
            print("Created 2 variables...")
        elif len(data[0]) == 3:
            for i in range(len(data)):
                    x.append(float(data[i][0]))
                    y.append(float(data[i][1]))
                    z.append(float(data[i][2]))
            return x, y, z
            print("Created 3 variables...")
        elif len(data[0]) == 4:
            for i in range(len(data)):
                x.append(float(data[i][0]))
                y.append(float(data[i][1]))
                z.append(float(data[i][2]))
                u.append(float(data[i][3]))
            return x, y, z, u
            print("Created 4 variables...")
        elif len(data[0]) == 5:
            for i in range(len(data)):
                x.append(float(data[i][0]))
                y.append(float(data[i][1]))
                z.append(float(data[i][2]))
                u.append(float(data[i][3]))
                v.append(float(data[i][4]))
            return x, y, z, u, v
            print("Created 5 variables...")
        elif len(data[0]) == 6:
            for i in range(len(data)):
                x.append(float(data[i][0]))
                y.append(float(data[i][1]))
                z.append(float(data[i][2]))
                u.append(float(data[i][3]))
                v.append(float(data[i][4]))
                w.append(float(data[i][5]))
            return x, y, z, u, v, w
            print("Created 6 variables...")
        elif len(data[0]) == 7:
            for i in range(len(data)):
                x.append(float(data[i][0]))
                y.append(float(data[i][1]))
                z.append(float(data[i][2]))
                u.append(float(data[i][3]))
                v.append(float(data[i][4]))
                w.append(float(data[i][5]))
                p.append(float(data[i][6]))
            return x, y, z, u, v, w, p
            print("Created 7 variables...")
        else:
            print("Something went wrong... :(")


def write_file ( fname, inpvec, names ):
    if len(inpvec) == 2:
        with open( fname, 'w') as file:
            writer = csv.writer( file, delimiter=' ')
            writer.writerow(names)
            for i in range(len(inpvec[0])):
                writer.writerow((inpvec[0][i], inpvec[1][i]))
        print("Wrote out 2 column data file...")
    elif len(inpvec) == 3:
        with open( fname, 'w') as file:
            writer = csv.writer( file, delimiter=' ')
            writer.writerow(names)
            for i in range(len(inpvec[0])):
                writer.writerow((inpvec[0][i], inpvec[1][i], inpvec[2][i]))
        print("Wrote out 3 column data file...")
    elif len(inpvec) == 4:
        with open( fname, 'w') as file:
            writer = csv.writer( file, delimiter=' ')
            writer.writerow(names)
            for i in range(len(inpvec[0])):
                writer.writerow((inpvec[0][i], inpvec[1][i], inpvec[2][i], inpvec[3][i]))
        print("Wrote out 4 column data file...")
    elif len(inpvec) == 5:
        with open( fname, 'w') as file:
            writer = csv.writer( file, delimiter=' ')
            writer.writerow(names)
            for i in range(len(inpvec[0])):
                writer.writerow((inpvec[0][i], inpvec[1][i], inpvec[2][i], inpvec[3][i], inpvec[4][i]))
        print("Wrote out 5 column data file...")
    elif len(inpvec) == 6:
        with open( fname, 'w') as file:
            writer = csv.writer( file, delimiter=' ')
            writer.writerow(names)
            for i in range(len(inpvec[0])):
                writer.writerow((inpvec[0][i], inpvec[1][i], inpvec[2][i], inpvec[3][i], inpvec[4][i], inpvec[5][i]))
        print("Wrote out 6 column data file...")
    else:
        print("Something went wrong... :(")
