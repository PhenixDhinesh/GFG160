# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

# Note: Consider the array as circular.

# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621

# took 22 min

from math import gcd

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction.

    # def rotateArr(self, arr, d):
    #     """
    #     Mine. solved by space extra used
    #     """
    #     arr_len = len(arr)
    #     d = d % arr_len
    #     arr_copy = arr.copy()

    #     for i in range(arr_len):
    #         arr[i] = arr_copy[(i + d) % arr_len]

    #     return

    def rotateArr(self, arr, d):
        """
        GFG solution, more efficient and uses less space O(1)
        """
        n = len(arr)
        d = d % n  # In case d > n
        g = gcd(n, d)

        for i in range(g):
            temp = arr[i]
            j = i

            while True:
                k = (j + d) % n
                if k == i:
                    break
                arr[j] = arr[k]
                print('j', j, 'k', k, 'i', i)
                j = k

            arr[j] = temp


"""
GFG expected algo - 2
"""
# Function to rotate an array by d elements to the left
def rotateArr(arr, d):
    n = len(arr)

    # Handle the case where d > size of array
    d %= n

    # Reverse the first d elements
    reverse(arr, 0, d - 1)

    # Reverse the remaining n-d elements
    reverse(arr, d, n - 1)

    # Reverse the entire array
    reverse(arr, 0, n - 1)

# Function to reverse a portion of the array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == '__main__' :

    arr = [1, 2, 3, 4, 5]
    d = 2
    obj = Solution()
    obj.rotateArr(arr, d)
    print(arr)

    arr = [1, 2, 3, 4]
    d = 2
    obj = Solution()
    obj.rotateArr(arr, d)
    print(arr)

    arr = [1, 2, 3, 4, 5]
    d = 4
    obj = Solution()
    obj.rotateArr(arr, d)
    print(arr)