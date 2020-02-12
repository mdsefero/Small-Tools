

print ""
name = raw_input("Enter file to parse (Enter for 'afile.csv'): ")
if len(name) == 0 : name = "afile.csv"
handle1 = open(name)
handle1.close()

masterlist = []
handle1 = open(name)
for line in handle1:
	line = line.strip("\n")
	line = "".join(line.split())
	line = line.split("_")
	temp = line[6]
	temp = temp[:-2]
	temp = "g_%s" % (temp)
	masterlist.append(temp)
handle1.close


append = "_out.csv"	
savename = name[:-4] + append
f = open(savename,'w')
for i, line in enumerate(masterlist): 
	f.write(line)
	if i < len(masterlist):
		f.write("\n")
f.close()
print ""
print "Saved as: ", savename