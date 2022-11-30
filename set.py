s = { 1,2,3,4,5,6,7,40,59}
s2 = { 5,6,7,30,59,40,24}

# 교집합
print(s & s2)
print(s.intersection(s2))

# 합집합
print(s | s2)
print(s.union(s2))


# add(), remove()


s.add(1010)
sr = s.remove(1010)
print(sr)
