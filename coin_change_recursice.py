# The coin change problem is a classic coding challenge that, when solved using dynamic programming, demonstrates both of DP's key principles: optimal substructure and overlapping subproblems.

# The coin change problem asks, "What's the minimum number of coins needed to make a target amount?"

def min_coins(amount, coins):
    """Find minimum number of coins needed to make the given amount"""
    # Initialize dp array with "infinity" - represents impossible to make
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # For each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:  # Can only use coin if it doesn't exceed current amount
                # Update minimum: current minimum vs (coins for remaining amount + 1)
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result if possible, -1 if impossible
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
# coins = [1, 3, 4], amount = 6
# dp[6] = min(dp[5]+1, dp[3]+1, dp[2]+1) = min(3+1, 1+1, 2+1) = 2
# Result: 2 coins (3 + 3)

# And here's how the dynamic programming coin change algorithm works step by step for coins = [1, 3, 4], amount = 6:

# Initial state:
# dp = [0, ∞, ∞, ∞, ∞, ∞, ∞]
#      [0, 1, 2, 3, 4, 5, 6] ← amounts

# Building up the solution:

# For amount = 1:
#   Try coin 1: dp[1] = min(∞, dp[0] + 1) = min(∞, 0 + 1) = 1
#   dp = [0, 1, ∞, ∞, ∞, ∞, ∞]

# For amount = 2:
#   Try coin 1: dp[2] = min(∞, dp[1] + 1) = min(∞, 1 + 1) = 2
#   dp = [0, 1, 2, ∞, ∞, ∞, ∞]

# For amount = 3:
#   Try coin 1: dp[3] = min(∞, dp[2] + 1) = min(∞, 2 + 1) = 3
#   Try coin 3: dp[3] = min(3, dp[0] + 1) = min(3, 0 + 1) = 1
#   dp = [0, 1, 2, 1, ∞, ∞, ∞]

# For amount = 4:
#   Try coin 1: dp[4] = min(∞, dp[3] + 1) = min(∞, 1 + 1) = 2
#   Try coin 3: dp[4] = min(2, dp[1] + 1) = min(2, 1 + 1) = 2
#   Try coin 4: dp[4] = min(2, dp[0] + 1) = min(2, 0 + 1) = 1
#   dp = [0, 1, 2, 1, 1, ∞, ∞]

# For amount = 5:
#   Try coin 1: dp[5] = min(∞, dp[4] + 1) = min(∞, 1 + 1) = 2
#   Try coin 3: dp[5] = min(2, dp[2] + 1) = min(2, 2 + 1) = 2
#   Try coin 4: dp[5] = min(2, dp[1] + 1) = min(2, 1 + 1) = 2
#   dp = [0, 1, 2, 1, 1, 2, ∞]

# For amount = 6:
#   Try coin 1: dp[6] = min(∞, dp[5] + 1) = min(∞, 2 + 1) = 3
#   Try coin 3: dp[6] = min(3, dp[3] + 1) = min(3, 1 + 1) = 2
#   Try coin 4: dp[6] = min(2, dp[2] + 1) = min(2, 2 + 1) = 2
#   dp = [0, 1, 2, 1, 1, 2, 2]

# Final result: dp[6] = 2 (achieved with coins 3 + 3)
# This solution demonstrates both key principles of dynamic programming. It has overlapping subproblems because finding the minimum coins for amount 6 requires knowing the solutions for amounts 5, 3, and 2. These same subproblems appear when calculating other amounts. It has optimal substructure because the optimal solution for any amount incorporates optimal solutions for smaller amounts. If we know the minimum coins for amount 3 is 1, then one way to make amount 6 is to use that solution plus one more coin of value 3.

# Without DP, we'd need to try every possible combination of coins - an exponential number of possibilities. With DP, we build up the solution systematically:

# Time complexity: O(amount × number of coins) instead of exponential.

# Space complexity: O(amount) for the dp array.

# No redundant work: Each subproblem (finding minimum coins for each amount) is solved exactly once.

# Reusable results: Once we know the minimum coins for amount 3, we use this knowledge for all larger amounts that can benefit from it.

