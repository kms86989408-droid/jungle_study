# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

spelling = input().upper()
lot = ""
max_count = 0

for i in set(spelling):
    cnt = spelling.count(i)
    if cnt > max_count:
        max_count = cnt
        lot = i
    elif cnt == max_count:
        lot = "?"

print(lot)