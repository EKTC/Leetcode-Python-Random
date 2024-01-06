# 34. Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given target value.

If the target is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```python
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
```

**Example 2:**

```python
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
```

**Example 3:**

```python
    Input: nums = [], target = 0
    Output: [-1,-1]
```

**Constraints:**

```python
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`
```

# Notes

- The general concept was achieved which is having to do two binary searches
- One to find the first position and another to find the last position and then checking if it is a valid range
- Side note that there is a Divide and Conquer possible solution
