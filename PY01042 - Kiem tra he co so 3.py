for _ in range(int(input())):
    s = input()
    print('YES' if all(char in ['0','1','2'] for char in s) else 'NO')