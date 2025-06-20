# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735

# Note: The second largest element should not be equal to the largest element.

# Example 1:

# Input: arr[] = {1, 2, 3, 4, 5}
# Output: 4
# Explanation: The largest element is 5 and the second largest element is 4.
# Example 2:

class Solution:
    def getSecondLargest(self, arr):
        """
        Get the second largest element from an array
        """
        # Code Here
        # My solution (already seen before, so did it easily)
        largest = arr[0]
        second_largest = -1

        for i in range(1, len(arr)):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]

            elif arr[i] < largest and arr[i] > second_largest:
                second_largest = arr[i]

        return second_largest

def getSecondLargest(arr):
    """
    GFG
    """
    n = len(arr)

    largest = -1
    secondLargest = -1

    # finding the second largest element
    for i in range(n):

        # If arr[i] > largest, update second largest with
        # largest and largest with arr[i]
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]

        # If arr[i] < largest and arr[i] > second largest,
        # update second largest with arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest

if __name__ == '__main__' :
    arr = [1, 2, 3, 4, 5]
    obj = Solution()
    print(obj.getSecondLargest(arr))  # Output: 4

    arr = [5, 5, 5]
    print(obj.getSecondLargest(arr))  # Output: -1