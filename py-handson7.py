#20,000以下の素数の和を求める

total = 0
max = 20000
for i in range(2, max + 1):
    for j in range(2, (i//2) + 1):
        if i % j == 0:
            break
    else:
        total += i
print(total)