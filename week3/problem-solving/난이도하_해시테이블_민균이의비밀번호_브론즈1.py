# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

n = int(input())
words = []
for i in range(n):
    words.append(input())
for word in words:
    reverse_word = word[::-1]

    if reverse_word in words:
        num_result = len(word)//2
        result = word[num_result]
        print(len(word), result)
        break







