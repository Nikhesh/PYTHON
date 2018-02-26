def find_length(l):
    length=len(l)
    del l
    return length
list=[1,2]
print find_length(list[:])
print list
