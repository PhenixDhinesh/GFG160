# You are given an array of integers arr[]. Your task is to reverse the given array.
# Note: Modify the array in place.

# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array

# Example 1:

# Input: arr[] = {1, 2, 3, 4, 5}
# Output: 5 4 3 2 1
# Example 2:

# Input: arr[] = {1, 2, 3}
# Output: 3 2 1

class Solution:
    def reverseArray(self, arr):
        """
        My Solution
        """
        # code here
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return arr



# alternative approaches mentioned in the blog
# def reverseArray(arr):
#     n = len(arr)

#     # Iterate over the first half and for every index i,
#     # swap arr[i] with arr[n - i - 1]
#     for i in range(n // 2):
#         temp = arr[i]
#         arr[i] = arr[n - i - 1]
#         arr[n - i - 1] = temp

# # recursive function to reverse an array from l to r
# def reverseArrayRec(arr, l, r):
#     if l >= r:
#         return

#     # Swap the elements at the ends
#     arr[l], arr[r] = arr[r], arr[l]

#     # Recur for the remaining array
#     reverseArrayRec(arr, l + 1, r - 1)

# # function to reverse an array
# def reverseArray(arr):
#     n = len(arr)
#     reverseArrayRec(arr, 0, n - 1)


if __name__ == '__main__' :
    arr = [1, 2, 3, 4, 5]
    obj = Solution()
    obj.reverseArray(arr)
    print(arr)

    arr = [1, 2, 3]
    obj.reverseArray(arr)
    print(arr)

    arr = [1, 2, 3, 2]
    obj.reverseArray(arr)
    print(arr)

    arr = [1]
    obj.reverseArray(arr)
    print(arr)