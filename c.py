array=[1,2,3,4]
i=0
a=[]
b=[]
c=[]
d=[]
while i<len(array):
    if array[i]==a:
        a.append(array)
        b.append(a,array)
        c.append(b,array)
        d.append(c,array)
    i+=1
print(array)

# O/p [1,[2,[3,[4]]]]