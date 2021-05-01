while True:
    N = int(input())
    if 1 < N < 100:
        break
for c in range(0, N):
    while True:
        K = int(input())
        if 1 < K < 50:
            break
    for l in range(0, K):
        Op = int(input())
        while not 0 < Op <= 4:
            Op = int(input())
        if Op == 1:
            print("Rolien")
        elif Op == 2:
            print("Naej")
        elif Op == 3:
            print("Elehcim")
        else:
            print("Odranoel")


