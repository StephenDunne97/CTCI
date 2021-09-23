"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator. 
Return the quotient after dividing dividend by divisor. 
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2. 

Example 1: 
################################################ 
Input: dividend = 10, divisor = 3 
Output: 3 
Explanation: 10/3 = truncate(3.33333..) = 3. 

Example 2: 
################################################ 
Input: dividend = 7, divisor = -3 
Output: -2 
Explanation: 7/-3 = truncate(-2.33333..) = -2. 

 Example 3: 
################################################ 

Input: dividend = 0, divisor = 1 
Output: 0 
Example 4: 
################################################ 
Input: dividend = 1, divisor = 1 
Output: 1 
Constraints: 
divisor != 0 
"""

def solution(dividend, divisor):
    result = dividend
    count = 0
    if divisor > 0:
        while result > 0:
            result = result - divisor
            if (result >= 0):
                count +=1
    elif divisor < 0:
        result = dividend - (dividend*2)
        divisor = -divisor
        while result < 0:
            result = result + divisor
            print(result)
            if (result <= 0):
                count -=1
    return (count)

print (solution(1, 1))
print (solution(10, 3))
print (solution(7, -3))
print (solution(0, 1))