def count_lower(n):
    return sum(map(str.islower,n))
t=input()
if count_lower(t)>=(len(t)/2):
    print(t.lower())
else:
    print(t.upper())