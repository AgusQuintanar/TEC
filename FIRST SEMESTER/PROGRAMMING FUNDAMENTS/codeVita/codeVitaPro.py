from math import factorial
import itertools
n = 12
mul = 0

for x in range(1,n+1):
    if n % x == 0:
        mul += 1
print(mul)
number_of_combinations = factorial(mul) - factorial(mul-1)*factorial(mul-2) - 1
print(number_of_combinations)





'''

 4! - (3!)(4-2)! -1  24 - 12 -1
 3! - (2!)(0)! -1 = 3
  
4x = 11  24 - 13
3x = 3   6 - 3
2x = 1   2 - 1

6 3 2 1 = 11
 // 9 3 1 = 3 //
  10 5 2 1 = 11 '''


