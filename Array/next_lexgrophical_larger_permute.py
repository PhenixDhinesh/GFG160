# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/next-permutation5226

# Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order).

# Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.


# took 74.45min
# chatgpt accidently gave the base logic

class Solution:
    def nextPermutation(self, arr):
        """
        Half Mine
        """
        arr_len = len(arr)

        temp_arr = None
        for i in range(arr_len - 2, -1, -1): # get from second last element
            if arr[i] < arr[i+1]:
                temp_arr = arr[:i]
                current_value = arr[i]
                current_arr = arr[i:]
                current_arr.sort()

                for j, value in enumerate(current_arr):
                    if value > current_value:
                        temp_arr.append(value)
                        current_arr.pop(j)
                        break

                temp_arr += current_arr

                for i in range(arr_len):
                    arr[i] = temp_arr[i]

                return

        arr.reverse()
        return

# Python Program to find the next permutation by
# generating only next
# GFG solution

def next_permutation(arr):
    n = len(arr)

    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break

    # If pivot point does not exist,
    # reverse the whole array
    if pivot == -1:
        arr.reverse()
        return

    # Find the element from the right
    # that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reverse the elements from pivot + 1 to the end in place
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


if __name__ == '__main__' :

    arr = [1, 2, 3]
    obj = Solution()
    obj.nextPermutation(arr)
    print(arr)

    arr = [2, 4, 1, 7, 5, 0]
    obj = Solution()
    obj.nextPermutation(arr)
    print(arr)

    arr = [3, 2, 1]
    obj = Solution()
    obj.nextPermutation(arr)
    print(arr)

    arr = [1, 2, 3, 6, 5, 4]
    obj = Solution()
    obj.nextPermutation(arr)
    print(arr)