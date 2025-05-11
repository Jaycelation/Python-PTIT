import sys

def decode_string(k, s):
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    return "".join(p[(p.index(c) + k) % 28] for c in reversed(s))

def main():
    while True:
        line = input().strip()
        if line == "0":
            break
        k, s = line.split()
        k = int(k)
        print(decode_string(k, s))

if __name__ == "__main__":
    main()