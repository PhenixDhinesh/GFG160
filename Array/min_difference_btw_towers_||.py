# Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

# Examples :

# Input: k = 2, arr[] = {1, 5, 8, 10}
# Output: 5
# Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.
# Input: k = 3, arr[] = {3, 9, 12, 16, 20}
# Output: 11
# Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11.

# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/minimize-the-heights3351

# TOOK 2+ hours, still did solve

# Take aways
# 1. sort the array
# 2. do greedy on partitioning the array to left and right
# Its new type of greedy that i haven't met yet, LEARNED

class Solution:
    def getMinDiff(self, arr,k):
        """
        GFG solution
        """

        n = len(arr)
        arr.sort()
        res = arr[n - 1] - arr[0]
        first = arr[0] + k
        last = arr[n - 1] - k

        for idx, value in enumerate(arr[1:], start = 1):

            if value - k < 0:
                continue

            minH = min(first, value - k)
            maxH = max(last, arr[idx - 1] + k)

            res = min(maxH - minH, res)

        return res


if __name__ == "__main__":
    k = 6
    arr = [12, 6, 4, 15, 17, 10]

    obj = Solution()
    ans = obj.getMinDiff(arr, k)
    print(ans)