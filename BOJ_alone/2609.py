import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
print(math.gcd(n, m))
print(math.lcm(n, m))