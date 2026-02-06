l = [5,4,3,2,1]
print(l)

# add something in the list
l.append(0)
print(l)

# sort in ascending orders
l.sort()
print(l)

# sort in descending orders
l.sort(reverse = True)
print(l)

# original list is reversed
l.reverse()
print(l)

# this method returns the index
print(l.index(0))

# count the number of times that item is in the list
print(l.count(3))

# returns the copy of the list
m = l.copy()
m[0] = 7
print(m)

# insert an item at a given index
l.insert(1,800)
print(l)

# extend method adds the entire list to the existing list
m = [900,600,800,400]
l.extend(m)
print(l)

# concatenate two lists
o = [9,8,7]
n = o + l
print(n)