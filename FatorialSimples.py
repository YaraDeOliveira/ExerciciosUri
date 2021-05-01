fat = 1
while True:
    N = int(input())
    if 0 < N < 13:
        break
for c in range(1, N+1):
    fat *= c
print(fat)

