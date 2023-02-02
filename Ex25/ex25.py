def is_present(data, n):
    for i in data:
        if n == i:
            return True
    return False

print(is_present([1, 5, 8, 3], 3))
print(is_present([5, 8, 3], -1))