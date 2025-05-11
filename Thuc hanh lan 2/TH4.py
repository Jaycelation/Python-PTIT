for _ in range(int(input())):
    n = input()
    val = n[len(n)-2] + n[len(n)-1]
    print("YES" if val == "86" else "NO")