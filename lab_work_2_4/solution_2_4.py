"""
Generate list with lowercase and uppercase alphabet plus numbers
"""
lst= ['J','U','S','t', 'd','o', 1, 2, 3, 4, 5 ]
"""
Print 1st symbol of list
"""
print(lst[0])
"""
Print last symbol
"""
print(lst[-1])
"""
Print 3rd from start and 3rd from the end
"""
print (lst[2],lst[-3])
"""
Slice first 10 symbols
"""
print(lst[:10])
"""
Print only symbols with index, which divides on 2 without remaining
"""
print(lst[2::2])
"""
Print only integer values from list
"""
digits=[]
for symbol in lst:
    try:
        digits.append(int(symbol))
    except ValueError:
        pass
    print(digits)
"""
 Reverse list using slice
"""
print(lst[::-1])
"""
Convert base list into string
"""
print(str(lst))