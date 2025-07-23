# ----------------------------------------------------
# Intuition:
#
# 1. Monotonic Stack (Optimized):
#    - Use a decreasing stack to keep indices of unresolved temperatures.
#    - When a warmer temperature is found, resolve previous days.
#    - Time: O(n), Space: O(n)
#
# 2. Two-Pass from Right (Less efficient but simple):
#    - Go from right to left, jump ahead using result array.
#    - Time: O(n^2) worst case, Space: O(1) if ignoring output
#
# 3. Brute Force:
#    - For each day, scan ahead to find the first warmer temperature.
#    - Time: O(n^2), Space: O(1)
# ----------------------------------------------------

from typing import List

class Solution:

    # ----------------------------------------------------
    # 1. Optimized Monotonic Stack
    # Time: O(n), Space: O(n)
    # ----------------------------------------------------
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Default all days to 0
        stack = []  # Stack to store indices of unresolved temps

        for curr_day, curr_temp in enumerate(temperatures):
            # Check if current temp is warmer than the last unresolved day
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day  # Found next warmer day
            stack.append(curr_day)  # Push current day for future comparison

        return answer

    # ----------------------------------------------------
    # 2. Two-Pass from Right (with jump-ahead using result array)
    # Time: O(n^2) worst, Space: O(1)
    # ----------------------------------------------------
    def dailyTemperatures_jump(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        for i in range(n - 2, -1, -1):  # Start from second last day
            j = i + 1
            # Jump ahead by using previously computed results
            while j < n and temperatures[j] <= temperatures[i]:
                if answer[j] == 0:
                    j = n  # No warmer day
                else:
                    j += answer[j]
            if j < n:
                answer[i] = j - i

        return answer

    # ----------------------------------------------------
    # 3. Brute Force
    # Time: O(n^2), Space: O(1)
    # ----------------------------------------------------
    def dailyTemperatures_bruteforce(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break  # Found warmer day, break inner loop

        return answer


# ----------------------------------------------------
# Example Usage and Test Cases:
# ----------------------------------------------------

if __name__ == "__main__":
    sol = Solution()

    print("Optimized Monotonic Stack:")
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
    print(sol.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
    print(sol.dailyTemperatures([30,60,90]))                 # [1,1,0]

    print("\nTwo-Pass with Jump:")
    print(sol.dailyTemperatures_jump([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]

    print("\nBrute Force:")
    print(sol.dailyTemperatures_bruteforce([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
