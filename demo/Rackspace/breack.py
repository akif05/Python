list1 = [5, 6, 7, 8, 2, -1, -2, -3, -6, -7]
total = 0
i = -1
while True:
    if list1[i] > 0:
        break 
    else:
        total += list1[i]
        i -= 1

print(f'Total: {total}');

