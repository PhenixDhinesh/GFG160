# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Example 1:

# Input: arr[] = {1, 2, 3, 4, 5}
# Output: 4
# Explanation: The largest element is 5 and the second largest element is 4.
# Example 2:

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = arr[0]
        second_largest = -1

        for i in range(1, len(arr)):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]

            elif arr[i] < largest and arr[i] > second_largest:
                second_largest = arr[i]

        return second_largest

if __name__ == '__main__' :
    arr = [1, 2, 3, 4, 5]
    obj = Solution()
    print(obj.getSecondLargest(arr))  # Output: 4

    arr = [5, 5, 5]
    print(obj.getSecondLargest(arr))  # Output: -1