# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys

n = int(sys.stdin.readline())
stack = []
result = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stack.append(command[1])

    elif command[0] == "pop":
        if len(stack) == 0:
            result.append("-1")
        else:
            result.append(stack.pop())

    elif command[0] == "size":
        result.append(str(len(stack)))

    elif command[0] == "empty":
        if len(stack) == 0:
            result.append("1")
        else:
            result.append("0")

    elif command[0] == "top":
        if len(stack) == 0:
            result.append("-1")
        else:
            result.append(stack[-1])

print("\n".join(result))
