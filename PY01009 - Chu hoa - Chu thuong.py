s = input()
count = 0
for i in s:
    if i.islower():
        count += 1
if count >= (len(s) - count):
    print(s.lower()) 
else:
    print(s.upper())