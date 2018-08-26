#Cumulative sum of a list [a, b, c, ...] is deﬁned as [a, a+b, a+b+c, ...] . Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?

def product(a):
    product=1
    for i in a:
        product=product*i
    return product

def csum(b):
    c=[]
    for i in b:
     slice_list=b[:b.index(i)+1]
     slicesum=product(slice_list)
     c.append(slicesum)
    print(c)

csum([1,2,3,4])
