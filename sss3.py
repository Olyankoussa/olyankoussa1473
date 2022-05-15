import json
infile='q3.json'
infile=open(infile,'r')
n=0
u=input('enter your name: ')
d=dict()
dic=json.load(infile)
infile.close()
for k,v in dic.items():
    print(k)
    x=input()
    if x == v:
        n+=1
        d[k]=v
d[u]=n
print(d)
outfile='ans3.json'
outfile=open(outfile,'w')
json.dump(d,outfile)
outfile.close()