s={}
print(type(s))

'''
methods
add
update
pop
remove
'''

s={2,3,34,43,4,4,4 }
print(s)

#add
s={2,3,34,43,4,4,4 }
s.add(123)
print(s)

#update
s={2,3,34,43,4,4,4 }
s.update({1,5,9,8})
print(s)

#pop
s={2,3,34,43,4,4,4 }
s.pop()
print(s)

#remove
s={2,3,34,43,4,4,4 }
s.remove(34)
print(s)

'''
operations
union
intersection
difference
issubset
issuperset
'''
#union
set1={11,22,33}
set2={44,55,66}
print(set1.union(set2))

#intersection
set1={111,222,333}
set2={222,444,555}
print(set1.intersection(set2))

#difference
set1={1000,1001,1002}
set2={1001,1000}
print(set1.difference(set2))

#issubset
set1={12,23,34,45,56,67,78,89,90}
set2={12,23}
print(set2.issubset(set1))

#issuperset
set1={12,13,14,15}
set2={12,13}
print(set1.issuperset(set2))

#for loop
for i in {1,2,3,4,}:
    print(i)