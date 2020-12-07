"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here
    '''
    Input: list of integer digits
    Output: list of integer digits representing the og number + 1 

    Plan 1: transform it into a single integer
                - join the list of integers into a single string 
                - change the single strong into an integer with the `int` function
            add one to our transformed integer (this takes care of carrying for us)
            transform the integer back into a list of digits

    Plan 2: Can we re-use the input to do waht we want to do?
            Can we just act on the input "digits" lists?
            [1,2,3] + 1  : add 1 to the last element in the list 
    '''

    #  iterate in reverse 
    for i in range(len(digits) - 1, -1, -1):
        #  check if the current digit == 9 
        if digits[i] != 9:
            digits[i] += 1
            # we are done; return our result
            return digits
        # otherwise, the current digit is 9 
        digits[i] = 0
    # if we reach outside of this for loop, then we got nothing but 9's 
    #  we need to add a 1 to the front of our list
    digits.insert(0,1)

    return digits

print(plus_one([9,9]))