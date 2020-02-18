import sys

lis =[]
key = sys.argv[1]
tn = sys.argv[2]
x = 0

for line in sys.stdin:
	lis.append(line[:-1])


print('{"'+tn+'":[')


print("{")
for line in lis:
	x+=1	
	if line.strip() != '\n':
		if line == lis[-1]:
				new = '"' + key + str(x) + '":"' + line + '"\n}'
				print(new)
		else:
			new = '"' + key + str(x) + '":"' + line + '",'
			print(new)

print("]}")
