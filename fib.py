def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def traditionalFib(n):
    if n <= 2:
        return 1
    return traditionalFib(n-1)+traditionalFib(n-2)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(50))
print(traditionalFib(25))
