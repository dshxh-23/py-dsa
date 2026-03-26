"""
REDO THE ENTIRE CODE AGAIN, WITHOUT SEEING THIS TIME
"""


def knapsack_01(p, w, capacity):
    n = len(w)      # no. of items

    # initializing the 2d table: rows represent first i items, columns represent the capacity to be filled
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n+1)]

    for i in range(1, n+1):                 # starting from index 1 cuz first row is entirely filled with zeros
        for maxm_w in range(1, capacity+1):      # starting from index 1 cuz the first col is also zeros

            # storing weight and profit of the element we'll decide to include or not for the cell 
            curr_w = w[i-1]
            curr_p = p[i-1]

            # skip item if it's weight is more then maximum weight
            if curr_w > maxm_w:
                dp[i][maxm_w] = dp[i-1][maxm_w]
            
            else:
                dp[i][maxm_w] = max(dp[i-1][maxm_w], curr_p + dp[i-1][maxm_w - curr_w])
        
    return dp[n][capacity]
            

def main():
    weights = [10, 20, 30]
    profits = [60, 100, 120]
    capacity = 50
    print(f"Max Value: {knapsack_01(profits, weights, capacity)}") # Output: 220  


if __name__ == "__main__":
    main()