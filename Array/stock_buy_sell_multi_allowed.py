# The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

# Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

# Example 1:

# Input: N = 7, price[] = {100,180,260,310,40,535,695}
# Output: 865
# Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210. Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655. Maximum Profit = 210 + 655 = 865.

from typing import List


# took 40.18min
# cleared in 1st attempt, the hint finding before logic building helped a lot for making sure of the algo

class Solution:
    def maximumProfit(self, prices) -> int:
        """
        Mine
        """
        arr_len = len(prices)
        # handle edge case
        if arr_len == 1:
            return 0

        left = 0
        right = 0
        profit = 0
        # hint: find all the continously incresing subarray and subtract edges
        for idx in range(1, arr_len):
            if prices[idx] <= prices[left] and left == right:
                right = idx
                left = idx
            elif prices[idx] >= prices[right]:
                right = idx
            else:
                profit += prices[right] - prices[left]
                right = idx
                left = idx

        # for final sub array
        profit += prices[right] - prices[left]

        return profit

# expected GFG approach
# DIFFERENT POINT OF VIEW
def maximumProfit(prices):
    res = 0

    # Keep on adding the difference between
    # adjacent when the prices a
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            res += prices[i] - prices[i - 1]

    return res


if __name__ == '__main__' :
    arr = [100, 180, 260, 310, 40, 535, 695]
    # arr = [4, 2, 2, 2, 4]
    # arr = [4, 3, 2, 1]
    obj = Solution()
    print(obj.maximumProfit(arr))

    print(maximumProfit(arr))