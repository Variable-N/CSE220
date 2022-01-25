def fibonacci (n,array = None):
    if array is None:
        array = [0]*(n+1)
    if array[n] != 0:
        return array[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    array[n] = fibonacci(n-1,array) + fibonacci(n-2,array)
    return array[n]

print(fibonacci(45))