import commands as c

l=c.getoutput("ls /dev/ttyS*")
lNombres=[]

lNombres=l.split('\n')

for i in range(len(lNombres)):
    print lNombres[i]