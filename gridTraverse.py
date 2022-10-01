def numWays(m, n):
    memo = {}
    return numWaysR(m, n, memo)

# Helper Recursive function, with memoization to increase runtime
def numWaysR(m, n, memo):
    key = str(m) + ',' + str(n)
    key2 = str(n) + ',' + str(m)
    if key in memo or key2 in memo:
        return memo[key] if key in memo else memo[key2];
    if m == 1 and n == 1:
        return 1;
    if m == 0 or n == 0:
        return 0;
    memo[key] = numWaysR(m-1, n, memo) + numWaysR(m, n-1, memo);
    return memo[key] 

print(numWays(1,1))
print(numWays(5,3))
print(numWays(14,12))
print(numWays(44,4))
print(numWays(4,2))
print(numWays(3,6))
print(numWays(100, 75))

