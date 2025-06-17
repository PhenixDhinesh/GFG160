# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote

# You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array.

# Note: The answer should be returned in an increasing format.

# took 40.12min

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        """
        Mine.

        >>> the key i missed was, if majority needs to more than n/3. there can be only two majorities
        """
        count = {}
        #Your Code goes here.

        for value in arr:
            if value not in count:
                count[value] = 1
            else:
                count[value] += 1

        sorted_count = sorted(count.items(), key=lambda x: x[1])

        # find the index where majority starts
        minimum_required_for_majority = len(arr) // 3
        start_idx = None
        for idx, value in enumerate(sorted_count):
            if value[1] > minimum_required_for_majority:
                start_idx = idx
                break

        if start_idx is None:
            return []

        return sorted([row[0] for row in sorted_count[start_idx:]])


# used moore's voting algo
# example
def majorityElement(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    # Verify the candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1


# GFG ans
# Python program for finding the majority element in
# an array using Moore’s Voting algorithm

def findMajority(arr):
    n = len(arr)

    # Initialize two candidates and their counts
    ele1, ele2 = -1, -1
    cnt1, cnt2 = 0, 0

    for ele in arr:
        # Increment count for candidate 1
        if ele1 == ele:
            cnt1 += 1
        # Increment count for candidate 2
        elif ele2 == ele:
            cnt2 += 1
        # New candidate 1 if count is zero
        elif cnt1 == 0:
            ele1 = ele
            cnt1 += 1
        # New candidate 2 if count is zero
        elif cnt2 == 0:
            ele2 = ele
            cnt2 += 1
        # Decrease counts if neither candidate
        else:
            cnt1 -= 1
            cnt2 -= 1

    res = []
    cnt1, cnt2 = 0, 0

    # Count the occurrences of candidates
    for ele in arr:
        if ele1 == ele:
            cnt1 += 1
        if ele2 == ele:
            cnt2 += 1

    # Add to result if they are majority elements
    if cnt1 > n / 3:
        res.append(ele1)
    if cnt2 > n / 3 and ele1 != ele2:
        res.append(ele2)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ")


if __name__ == '__main__' :
    arr = [1, 2, 3, 4, 5]
    obj = Solution()
    print(obj.findMajority(arr))

    arr = arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
    obj = Solution()
    print(obj.findMajority(arr))

