# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

n = int(input())

for i in range(n):
    R, S = input().split()
    R = int(R)
    
    result = ""

    for j in S:
        result += j * R
    print(result)

