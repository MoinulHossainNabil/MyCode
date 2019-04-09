import sys
filename=sys.argv[1]
fileCopies=int(sys.argv[2])
filenames =[]
for x in range(fileCopies):
    print("iteration number : {a}".format(a=x))
    filenames.append(filename)    	
with open('ratings-{a}.csv'.format(a=fileCopies), 'w') as outfile:
    count=0 
    for fname in filenames:
        count=count+1
        print("Started {a}".format(a=count))
        with open(fname) as infile:
            for line in infile: 
                outfile.write(line)
