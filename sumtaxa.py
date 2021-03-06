
# This program does running addition of OTU relatave abundance 
# and reorganizes columns from files output from taxaparsing.py 


import sys

def strp (var):
	var = var.strip("\t")
	var = var.strip("\n")
	var = "".join(var.split(" "))
	var = "".join(var.split("'"))
	var = "".join(var.split(")"))
	var = "".join(var.split("("))
	var = "".join(var.split("]"))
	var = "".join(var.split("["))
	return var

print " "
name = raw_input("Enter nodes file (Enter for 'IHCPWGS.csv'): ")
if len(name) == 0 : name = sys.argv[1]
handle1 = open(name)
handle1.close()



taxa = dict()
handle1 = open(name)
#handle1.readline()
for line in handle1:
	RA = list()
	line = strp(line)
	if line[:1] == "_": 
		line = line.split(",")
		OTU = line[0]
		for i in xrange(3,11):
			#print i, line[i]
			RA.append(float(line[i]))  
		if OTU in taxa.keys(): 
			for i in xrange(8):
				taxa[OTU][i] += RA[i] 
		else: 
			taxa[OTU] = RA
handle1.close()

#for keys, values in taxa.items(): 
#	print keys
#	print values

sortedlist = list()
for k,v in taxa.items():
	temp = "g" + k + "," + str(v)
	temp = strp(temp)
	sortedlist.append(temp)
sortedlist.sort(key=lambda l: float(l.split(',')[8]))#,reverse=True)

for i in sortedlist:
	print i


print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'IHCPWGS_taxa_OTUra.csv'): ")
#if len(savename) == 0: quit()
if savename == "d": savename = "IHCPWGS_taxa_OTUra.csv"
else: savename = savename + ".csv"
if len(savename) != 0:
	f = open(savename,'w')
	f.write("OTU,Cluster 1,Cluster 2,Cluster 3,Cluster 4,IHCP,Treated,GUDCA +,All\n")
	for values in sortedlist:
		f.write(values)
		f.write("\n")
	f.close()
	print "Saved as:", savename	
	
	
#test = raw_input("Format for bubble plot? (Y/N) :")
#if test != "y" and test != "Y":
#	quit()
	
bpformat = list()
groups = ('Taxa','.Cluster 1','.Cluster 2','.Cluster 3','.Cluster 4','.IHCP','.Treated','.GUDCA +','.All')

newline = "Taxa\tCategory\tAbundance\tIndVal"
bpformat.append(newline)


for i in sortedlist:
	line = i.split(',')
	for x in xrange(1,9):
		newline = "%s\t%i%s\t%s\t0.0" % (line[0], x, groups[x], line[x])
		bpformat.append(newline)

for i in bpformat: 
	print i	

indicator = 0	
lastline = ""		
n = 0
char1 = 0	
char2 = -1 	
alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print "bpformat", len(bpformat)
print "alf", len(alf)**2
if len(bpformat) >> (len(alf)**2):
	indicator = 1
else:
	while (n < len(bpformat)):
		#print n, bpformat[n]
		line =  bpformat[n].split('\t')
		if line[0] != "Taxa":
			if line[0] != lastline:
				char2 = char2 + 1
				#print "New taxa"
			bpformat[n] = "%s%s  %s" % (alf[char1], alf[char2], bpformat[n])
		print n, bpformat[n]
		lastline = line[0]
		print float(char2)/len(alf), char2, len(alf)
		if ((float(char2 + 1))/len(alf)).is_integer() == True:
			print "yes"
			if ((char2 + 1) /len(alf)) != 0:
				char1 = char1+1
				char2 = -1
		n = n + 1

	
for i in bpformat: 
	print i

if indicator >> 0: 
		print "\nWARNING: Not enough labels for all taxa - order will not be preserved" 
	
	
print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'BubblePlot_Data.txt'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "BubblePlot_Data.txt"
else: savename = savename + ".txt"
f = open(savename,'w')
for values in bpformat:
	f.write(values)
	f.write("\n")
f.close()
print "Saved as:", savename	
	
