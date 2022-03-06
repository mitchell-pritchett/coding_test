print("-"*30)
print('using sorted()')
x = [6,4,3,7,1]
print('before sorting:')
print(x)
print('ascending:')
print(sorted(x))
print('descending:')
print(sorted(x, reverse=True))

print('if you want to sort tuple, which is immutable\nfirst use sorted() and get sorted list returned\nthen make it tuple.')
t = (3,4,2,6)
print(t)
print(f'tuple(sorted({t}))=',tuple(sorted(t)))