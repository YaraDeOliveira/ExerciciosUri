while True:
    N = int(input())
    if 5 < N < 2000:
        break
for c in range(1, N+1):
    if c % 2 == 0:
        print(f'{c}^2 = {c**2}')


