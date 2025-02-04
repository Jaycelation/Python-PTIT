n = int(input())
arr = list(map(int, input().split()))

stack = []
stack.append(arr[0])

for i in range(1, n):
    val = arr[i]
    if stack and (stack[-1] + val) % 2 == 0:
        stack.pop()
    else:
        stack.append(val)

print(len(stack))