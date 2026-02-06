# Joining Sets                                                                                                          
# union and update
a = {1,2,3,4}
b = {2,8,9,6}
print(a,b)
print(a.union(b))
a.update(b)
print(a)
print(b)

# intersection and intersection update
c = {1,2,3}
d = {2,3,5}
print(c.intersection(d))
c.intersection_update(d)
print(c,d)

# symmetric difference and symetric_difference_update
e = {2,3,5,8}
f = {5,2,8,7}
print(e.symmetric_difference(f))
e.symmetric_difference_update(f)
print(e,f)

# difference() and difference_update()
g = {1,2,3}
h = {1,8,6}
print(g.difference(h))
g.difference_update(h)
print(g,h)

# isdisjoint()
i = {12,2,38,4}
j = {1,8,3,6}
print(i.isdisjoint(j))

# issuperset()
k = {1,2}
l = {2,1}
print(k.issuperset(l))

# add()
m = {9,8,7,4}
m.add(2)
print(m)

# update()
n = {1,2,3}
o = {9,8,7}
n.update(o)
print(n)

# remove()/discard()
p = {1,5,6}
p.remove(5)
print(p)

p.discard(7)
print(p)

# pop()
q = {1,9,8,5}
r = q.pop()
print(q)
print(r)

# del()
s = {1,2,3}
del s

# clear()
t = {1,2,3}
t.clear()
print(t)