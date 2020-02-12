name = input("Enter file to append string (Enter for 'file.csv'): ")
if len(name) == 0 : name = "References_RC2_A1_finallll.txt"

handle1 = open(name)
list = list()
for line in handle1: list.append(line.lstrip('0123456789.-*\t '))
handle1.close()

f = open(name [:-4] + "_formated.txt",'w')
for values in list: f.write(values)
f.close()
