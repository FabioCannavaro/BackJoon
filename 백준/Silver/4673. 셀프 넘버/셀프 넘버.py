def self_num(a):
    all_num=[]
    no_self_num=[]
    for i in range(a):
        all_num.append(i)
        no_i=i+sum(map(int, str(i)))
        no_self_num.append(no_i)
    selfnum=list(set(all_num)-set(no_self_num))
    selfnum.sort()
    return selfnum

result = self_num(10000)
output = '\n'.join(map(str, result))
print(output)