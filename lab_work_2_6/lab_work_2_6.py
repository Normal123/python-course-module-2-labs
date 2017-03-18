"""
Generate two sets with not unique numbers and few symbols
"""
x1= set('python12345')
x2= set('hello987654')
"""
Print 1st set
"""
print(x1)
"""
Create tuple from intersection of first and second set
"""
tup1= tuple(set(x1)&set(x2))
print(tup1)
"""
Create tuple from difference first and second set
"""
tup2 = tuple(x1-x2)
print(tup2)
"""
Slice first 3 symbols from first tuple
"""
print(tup1[0:3])
"""
Print only symbols with numbers from second set
"""
digits = []
mylist = str(x1)+str(x2)
for symbol in mylist :
    try:digits.append(int(symbol))
    except ValueError:
        pass
print(digits)
"""
Reverse tuple using slice
"""
print(tup1[::-1])
print(tup2[::-1])
"""
Convert both tuples into list
"""
print(list(tup1))
print(list(tup2))

