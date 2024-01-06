# ============== Solution 1 ================= # 2
# So for this its performing two binary searches but for the binary search iteration
# We want to find / ensure that the left pointer is pointing at the position of the first instance of the target value
# Hence why when we get a condition where we would normally shift the right pointer down by mid - 1 but instead theres another case
# Normally we have a `mid = target` case but here that implies that it is either at mid or on the left side
# So we combine the case to just be `right = mid`
#
# The return statement clicks all together as we want to find the first & last meaning the leftmost occurence and rightmost occurence
# And our binary search finds the leftmost occurence of a target value we can then make it such that we can perform one binary search on the target
# And another binary search on the target + 1 as that will give the leftmost occurence of hte next value and then -1 to that to get the actual last index
# This feels like a hacky method with that -1 trick but its absolutely brilliant way of solving it
#
# Time Complexity: 2 * log(n) =>O(log n)
# Space Complexity: O(1)
def searchRange(nums, target):
        def search(n):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= n:
                    right = mid
                else:
                    left = mid + 1
            return left

        left = search(target)
        return [left, search(target + 1) - 1] if target in nums[left:left + 1] else [-1, -1]

if __name__ == '__main__':
    print(searchRange([1,2,3,3,4,5,6,7,7,7], 7))

