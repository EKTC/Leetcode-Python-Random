# Use of a slower pointer that only updates
# On a condition we set -> in this case when the value in the array does not match the `val` variable
# We return how many elements there are that are not the `val` variable
#
# Time Complexity: O(n) where `n` is the length of array
# Space Complexity: O(1) no extra space was used
def removeElement(nums, val) -> int:
    slow = 0
    for number in nums:
        if number != val:
            nums[slow] = number
            slow += 1
        
    return slow