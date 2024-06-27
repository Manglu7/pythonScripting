import os
import os.path
import shutil

#os.mkdir('folder1')
#a = os.listdir('.')
#print(a)

#with open('folder1/file1.txt', 'a'):
 #   pass

#with open('folder1/file2.txt', 'a'):
 #   pass



#x = os.path.exists('.venv')
#print(x)

#os.rmdir('folder1')
#a = os.listdir('.')
#print(a)

shutil.rmtree('folder1')
a = os.listdir('.')
print(a)