file = open('sample.txt', 'r')
file2 = open('sample.txt','w')
#content = file.read()
line = file.readline()
lines = file.readlines()
#print(content)
print(line)
print(lines)
file2.writelines('this is the writing of a line\n')
