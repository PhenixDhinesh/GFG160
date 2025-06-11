# You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.


# NOTE: need to reduce time complexity
# currently,
# Worst-case (Big-O):
# O(n^2) — occurs when all elements are zeros at the start (every pop(i) takes O(n), done n times).

# Average-case (Theta):
# Θ(n^2) — on average, about half of the elements being zeros spread across the array still causes frequent pop(i) operations.

# Best-case (Omega):
# Ω(n) — when no zeros are present, the loop just iterates n times with constant operations.

# TOOK 31.24min

class Solution:

    # MINE
    # def pushZerosToEnd(self, arr:list):

    #     length = len(arr)
    #     i = 0
    #     traversed = 0
    #     while traversed < length:
    #         if arr[i] == 0:
    #             arr.append(arr.pop(i))
    #         else:
    #             i += 1

    #         traversed += 1

    def pushZerosToEnd(self, arr:list):
        """
        SOLUTION FROM GFG, not solved by me
        """

        count = 0
        for i, value in enumerate(arr):
            if value != 0:
                arr[count], arr[i] = arr[i], arr[count]
                count += 1

        return arr


if __name__ == '__main__' :
    arr = [0, 1, 0, 3, 12]
    obj = Solution()
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [1, 3, 12, 0, 0]

    arr = [0, 0, 0]
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [0, 0, 0]

    arr = [1, 2, 3]
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [1, 2, 3]

    arr = [3, 5, 0, 0, 4]
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [1, 2, 3]

    arr = [0, 1, 0, 3, 12, 0, 5, 0, 0, 9, 8]
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [1, 3, 12, 5, 9, 8, 0, 0, 0, 0, 0]

    arr = [0, 0, 0, 1]
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [1, 0, 0, 0]

    arr = [4, 0, 5, 0, 0, 6, 0, 7, 8, 0, 0, 9]
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0]

    arr = [10, 0, 0, 0, 20, 0, 30, 0, 0, 40, 0]
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [10, 20, 30, 40, 0, 0, 0, 0, 0, 0, 0]

    arr = [0, 0, 0, 0, 0, 0, 1]
    obj.pushZerosToEnd(arr)
    print(arr)  # Output: [1, 0, 0, 0, 0, 0, 0]

