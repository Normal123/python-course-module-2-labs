-  ##Laboratory Work 2.1.
+  ##Laboratory Work 2.2.

####Description:

Write the code to do following:

- Generate sequence 5 integers long from range(0, 100)
- Generate random f- Print
variables
above
- Find
max
element
from generated sequence

- Make
a
floor
division
between
max
element and generated
float
- Find
factorial
of
the
result
above
- Shorten
the
code as much as possible

####Here is its solution code:

*solution_2_2.py *
```python
import random
import math

"""
Generate sequence 5 integers long from range(0, 100)
"""
print('5 integers from range(0, 100): {}'.format(random.sample(range(100), 5)))

"""
Generate random float
Print variables above
"""

generated_float = random.random()
print('Generate random float: {}'.format(generated_float))

"""
Find max element from generated sequence
"""

sequence = random.sample(range(100), 5)
max_in_sequence = max(sequence)
print('Max element of {} is {}'.format(sequence, max_in_sequence))

"""
Make a floor division between max element and generated float
"""

floor_division = max_in_sequence // generated_float
print('floor division between max element ({}) and generated float ({}): {}'
      .format(max_in_sequence, generated_float, floor_division))

"""
Find factorial of the result above
"""

print('Factorial of the result above is:{}'.format(math.factorial(floor_division)))

```