import os

for i in range(97,123):
    os.mkdir('./crop/'+chr(i))

for i in range(10):
    os.mkdir('./crop/'+str(i))
print 'done'
