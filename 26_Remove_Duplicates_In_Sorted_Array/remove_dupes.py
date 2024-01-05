# ================= Solution 1 =============== #
# My first solution which i knew was quite naive and brute force ish
# The idea is to just grab all the unique numbers from the list
# And then afterwards replacing it with another loop
# 
# Though the second loop can be short it can be also the entire length of the list which in worst case is n^2 time complexity
#
# Time Complexity: O(k * n) where `n` is the length of the given list / array and `k` is the length of our second array storing the unique numbers
# Space Complexity: O(k) where `k` is the number of elements we are holding
def removeDuplicates(nums) -> int:
    unique_numbers = []

    for index, number in enumerate(nums):
        if number not in unique_numbers:
            unique_numbers.append(number)
        
        nums[index] = 0

    count = 0
    for value in unique_numbers:
        nums[count] = value
        count += 1

    return len(unique_numbers)

# ================= Solution 2 =============== #
# This second solution is much more faster and does not use any extra space
# The general idea is to use two pointers ah yes -> I need to realise that when your dealing with arrays two pointers is really useful
# Now its not a left / right setup of two pointers but i think of it as fast / slow pointers
# Where we update the slow pointer only when we find a new number to add to the set
# The fast pointer constantly moves and as a result will reach the end of the list where we can end the algorithm
#
# Time Complexity: O(n) where `n` is the length of array
# Space Complexity: O(1) no extra space was used
def removeDuplicatesV2(nums) -> int:
    slow = 0

    for fast in range(0, len(nums)):
        # Checks if the value is unique and we can add
        # Shifts the pointer to add the new value
        if nums[slow] != nums[fast]: 
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1