for _ in range(int(input())):
    n = input()
    val = 0
    for i in range(len(n)):
        val += int(n[i])
    print("YES" if val % 3 == 0 else "NO")