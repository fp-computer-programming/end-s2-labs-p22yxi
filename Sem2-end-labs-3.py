# Yongdong Xi
# findNextSquare
import math
def find_Next_Square():
    # find_Next_Square
    c = int(input("What is the first perfect square? "))
    # Get the next perfect square you need to find
    a = int(math.sqrt(c))
    if a * a == c:
        b = a + 1
        d = b * b
        print(d)
    else:
        print("-1 since {0} is not a perfect square".format(c))
    