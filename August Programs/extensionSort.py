def charcount(filename):
    return len(open(filename).read().split()
print(charcount("hello.txt"))
