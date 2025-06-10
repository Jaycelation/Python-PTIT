for _ in range(int(input())):
    s = input()
    dem = {}
    val = {}
    cnt = 1
    for i in range(len(s)):
        dem[s[i]] = dem.get(s[i], 0) + 1
        if s[i] not in val:
            val[s[i]] = cnt
            cnt += 1
        else:
            continue
    max_val = max(dem.values())
    for key, value in val.items():
        if dem[key] == max_val:
            print(key, end=' ')
            break
    print()