for _ in range(int(input())):
    n = input()
    val = 1
    sum = 0
    for i in range(len(n)):
        if i % 2 == 1:
            sum += int(n[i])
        else:
            if int(n[i]) != 0:
                val *= int(n[i])
    if sum == 0:
        print("INVALID")
    else:
        print(f"{val / sum:.6f}")