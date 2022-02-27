l = list('abcdefg')
t = tuple('abcdefg')

for i in l:
    print(i)

for j in t:
    print(j)

print("reversed")
for ri in reversed(l):
    print(ri)

for rj in reversed(t):
    print(rj)

print("[::-1]")
for rii in l[::-1]:
    print(rii)

for rjj in t[::-1]:
    print(rjj)