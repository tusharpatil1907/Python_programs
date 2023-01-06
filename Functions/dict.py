str1=input("Enter string: ")
l=str1.split()
d={}
for w in l:
    if w[0] not in d.keys():
        d[w[0]]=[]
        d[w[0]].append(w)
    else:
        if(w not in d[w[0]]):
            d[w[0]].append(w)
for k,v in d.items():
    
    print(k,":",v)


"""
Enter string: Tushar patil shahada
T : ['Tushar']
p : ['patil']
s : ['shahada']
"""