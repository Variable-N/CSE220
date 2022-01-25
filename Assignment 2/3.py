def hocBuilder(height):
    if height == 0:
        return 0
    if height == 1:
        return 8
    return 5+hocBuilder(height-1)

print(hocBuilder(3))