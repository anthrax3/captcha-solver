import os

for i in range(97,123):
    os.mkdir('./tem/'+chr(i))

for i in range(97,123):
    os.mkdir('./tem/'+chr(i).upper()+"1")

for i in range(10):
    os.mkdir('./tem/'+str(i))


print 'done'
