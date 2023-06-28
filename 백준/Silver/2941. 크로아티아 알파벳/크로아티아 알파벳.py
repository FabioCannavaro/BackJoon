croatic=["c=", "c-", "dz=", "d-", 
             "lj", "nj", "s=", "z="]
s=input()
cnt=0
for i in croatic:
    s=s.replace(i,'1')
print(len(s))