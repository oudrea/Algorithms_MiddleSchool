
import math


def factorial(n: int) -> int:
   result = 1
   for frogg in range(1,n):
      result=frogg*result
   return result    
# result starts at 1
# frogg starts at 1
# result becomes frogg * result , 1 * 1 = 1
# frogg becomes 2
# result becomes 2 * old result, 2 * 1 = 2
# frogg becomes 3
# result becomes 3 * old result, 3 * 2 = 6
# frogg becomes 4
# result becomes 4 * 6 = 24
# frogg becomes 5
# result becomes 5 * 24 = 120


def factorial2(n: int) -> int:
    return math.nan if n <= 0 else 1 if n==1 else n * factorial2(n-1)


if __name__ == '__main__':
   n = int(input("Enter n:"))
   print(f"{n}!={factorial2(n)}")#, method 2 is {factorial2(n)}")
