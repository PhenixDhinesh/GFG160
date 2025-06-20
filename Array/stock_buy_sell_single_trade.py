# Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

# Note: Stock must be bought before being sold.

# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2


# took 59min

class Solution:
    def maximumProfit(self, prices):
        """
        Mine
        """

        arr_len = len(prices)
        profit = 0

        if arr_len <= 1:
            return profit

        smallest = prices[0]
        biggest = prices[0]

        for idx in range(1, arr_len):
            # check if prices decending, if yes
            # get to the lowest possible price
            if prices[idx - 1] > prices[idx]:
                # dont perform calculation on same index
                if smallest != biggest:
                    profit = max(biggest - smallest, profit)

                if prices[idx] < smallest:
                    smallest = prices[idx]
                    biggest = prices[idx]

            else:
                # change the biggest accordingly
                biggest = prices[idx]

        profit = max(biggest - smallest, profit)

        return profit


# GFG solution
def maxProfit(prices):
    """
    simple and efficient
    """
    minSoFar = prices[0]
    res = 0

    # Update the minimum value seen so far
    # if we see smaller
    for i in range(1, len(prices)):
        minSoFar = min(minSoFar, prices[i])

        # Update result if we get more profit
        res = max(res, prices[i] - minSoFar)

    return res


if __name__ == '__main__' :
    arr = [100, 180, 260, 310, 40, 535, 695]
    # arr = [4, 2, 2, 2, 4]
    # arr = [4, 3, 2, 1]
    # arr = [7, 1, 5, 3, 6, 4]
    arr = [79, 2, 57, 33, 13, 51]
    obj = Solution()
    print(obj.maximumProfit(arr))