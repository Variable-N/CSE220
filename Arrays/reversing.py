
def reverse (source):
    i = 0
    j = len(source)-1
    while (i<j):
        source[i] = source[j] + source[i]
        source[j] = source[i] - source[j]
        source[i] = source[i] - source[j]
        i += 1
        j -= 1
    return source



a = [10,20,30,40,50]
reverse(a)
print(a)