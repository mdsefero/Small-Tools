
# This program organizes and labels data by taxa

import sys

def strp (var):
	var = var.strip("\t")
	var = var.strip("\n")
	return var

print " "
name = raw_input("Enter nodes file (Enter for 'IHCPWGS.csv'): ")
if len(name) == 0 : name = sys.argv[1]
handle1 = open(name)
handle1.close()

n=0
taxa = list()
handle1 = open(name)
#handle1.readline()
for line in handle1:
	line = strp(line)
	print line
	if n == 0:
		line = "," + line
	else:
		line = line.split("g_")
		OTU = line[1].split(";")
		OTU = OTU[0]
		line = OTU + "," + line[0] + "g_" + line[1]
	taxa.append(line)
	n=n+1
handle1.close()
	
#for i in taxa: 
#	print i

print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'IHCPWGS_taxa.csv'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "IHCPWGS_taxa.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
for values in taxa:
	f.write(values)
	f.write("\n")
f.close()
print "Saved as:", savename	
	
