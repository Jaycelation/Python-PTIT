from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = Counter(a)

freq_values = sorted(set(freq.values()), reverse=True)
if len(freq_values) < 2:
    print("NONE")
else:
    second_max_freq = freq_values[1]
    candidates = [num for num in range(1, k+1) if freq[num] == second_max_freq]
    if candidates:
        print(min(candidates))
    else:
        print("NONE")