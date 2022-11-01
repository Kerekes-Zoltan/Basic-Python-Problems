def count(numbers):
    cnt = 0
    
    for number in numbers:
        if number == 4:
            cnt += 1
    return cnt

print(count([1, 2, 4]))