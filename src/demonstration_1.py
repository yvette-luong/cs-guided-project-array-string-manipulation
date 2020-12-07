"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    # Your code here
    '''
    Input: List of integers
    Output: an int, the pivot index (note that we dont count the value at the pivot)

    Plan 1: Loop through each number 
            Get the sum of all numbers to this number's left side
            Get the sum of all numbers to this number's right side
            If the 2 sumns match, return the index of the current number 

    this plan works, but we perform a lot of redundant summing
    Because of the fact that we're touching every other number except the current number, for every single number in the list , this is an O(n^2) solution


    Plan 2: keep track of the total sum of the list 
            keep track of the current running sum as we iterate 
            iterate thorugh our numbers 
            subtract the current number from the total 
            check if the new total = running sum 
                if it does -> return the index of the current number
    '''
    # O(n) + O(n) = O(2*n) ~ O(n)time

    total = sum(nums) #in O(n) Time 
    running = 0

    for i,num in enumerate (nums): #O(n) run through every single nums 
        # O(1)
        # subtract num from total 
        total -= num 
        # check if total == running 
        if total == running:
            # return the index of num 
            return i 

        running += num 

    return -1

# nums = [1,7,3,6,5,6]
nums = [1,2,3]
print(pivot_index(nums))
