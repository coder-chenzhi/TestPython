count = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i + j + k == 9:
                print i , j , k
                count += 1
print count
