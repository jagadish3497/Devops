nl=[]
for x in range(10, 100):
    if ((x%7)==0)  and ((x%5)!=0):
        nl.append(str(x))
print (','.join(nl))