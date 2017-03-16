"""
 Generate string with lowercase and uppercase alphabet plus numbers
"""
St = "VHFtkh34"

"""
Print 1st symbol of string

"""
print (St[0])

"""
Print last symbol

"""
print (St[-1])

"""
Print 3rd from start and 3rd from the end

"""
print (St[2], St[-3])
"""
Slice first 8 symbols

"""
print(St[:8])
"""
Print only symbols with index, which divides on 3 without remaining

"""
print(St[3::3])
"""
 Print the symbol of the middle of the string text

"""
print (St[len(St) // 2])
"""
 Reverse text using slice

"""
print(St[::-1])