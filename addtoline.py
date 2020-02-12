
# This program appends a string at the end of a line. 

def strp (var):
	var = var.strip(" ")
	var = var.strip("\n")
	return var

print " "
name = raw_input("Enter file to append string (Enter for 'file.csv'): ")
if len(name) == 0 : name = "file.csv"
handle1 = open(name)
handle1.close()
print "\n"
string = raw_input("Enter the string you want added to each line: ")


list = list()

handle1 = open(name)
for line in handle1:
	line = strp(line)
	newline = line + string
	list.append(newline)
handle1.close()

print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'fileNew.csv'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "fileNew.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
for values in list:
	f.write(values)
	f.write("\n")
f.close()
print "Saved as:", savename	
	
