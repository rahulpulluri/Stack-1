# ----------------------------------------------------
# Intuition:
#
# 1. Monotonic Decreasing Stack (Optimized):
#    - Traverse the array twice to simulate circular array.
#    - Use a stack to maintain indices of decreasing elements.
#    - For each element, if it’s greater than stack top, update result.
#    - Only push index in the first pass.
#    - Time: O(n), Space: O(n)
#
# 2. Naive Brute Force:
#    - For each element, scan next n-1 elements circularly.
#    - Time: O(n^2), Space: O(n)
# ----------------------------------------------------

from typing import List

class Solution:

    # ----------------------------------------------------
    # 1. Monotonic Stack (Optimized Circular NGE)
    # Time: O(n), Space: O(n)
    # ----------------------------------------------------
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]] < curr:
                idx = stack.pop()
                res[idx] = curr
            if i < n:
                stack.append(i)
        
        return res

    # ----------------------------------------------------
    # 2. Naive Brute Force
    # Time: O(n^2), Space: O(n)
    # ----------------------------------------------------
    def nextGreaterElements_brute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            for j in range(1, n):
                next_idx = (i + j) % n
                if nums[next_idx] > nums[i]:
                    res[i] = nums[next_idx]
                    break
        return res

# ----------------------------------------------------
# Example Usage:
# ----------------------------------------------------

if __name__ == "__main__":
    sol = Solution()
    print("Optimized Monotonic Stack:")
    print(sol.nextGreaterElements([1, 2, 1]))     # [2, -1, 2]
    print(sol.nextGreaterElements([1, 2, 3, 4, 3])) # [2, 3, 4, -1, 4]

    print("\nBrute Force:")
    print(sol.nextGreaterElements_brute([1, 2, 1]))     # [2, -1, 2]
    print(sol.nextGreaterElements_brute([1, 2, 3, 4, 3])) # [2, 3, 4, -1, 4]
