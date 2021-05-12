#alfabeto = ("A", "B" "C" "D" "E" "F" "G" "H" "I" "J" "K", "L" "M" "N" "O P Q R S T U V X Z)
import string
c = 1
alfabeto = list(string.ascii_uppercase)
n = int(input())
for d, v in enumerate(alfabeto, start=1):
    print(v*d)
    if c == n:
        break
    else:
        c += 1