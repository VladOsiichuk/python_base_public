"""
n = 3
  **  
 **** 
******
"""

n = int(input("Enter n: "))

for i in range(1, n+1):
    stars = "*" * i * 2
    whtitespaces = " " * (n - i)
    print(whtitespaces + stars)