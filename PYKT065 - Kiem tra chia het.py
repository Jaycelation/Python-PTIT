while True:
    try:
        line = input().strip()
        if line == "-1":
            break

        L, R = map(int, line.split())
        n = int(input())

    except EOFError:
        break

#Hard