numbers = []
seen = set()  # Dùng để kiểm tra số trùng
count = 0  # Đếm số trùng + số không chia hết cho 42

while len(numbers) < 10:
    for num in map(int, input().split()):  
        if len(numbers) >= 10:
            break  # Dừng nếu đã đủ 10 số
        if num in seen:
            count += 1  # Nếu số trùng, tăng count
        numbers.append(num)  # Thêm vào danh sách (dù trùng hay không)
        seen.add(num)  # Đánh dấu số đã xuất hiện

# Đếm số không chia hết cho 42
count += sum(1 for i in numbers if i % 42 != 0)

print(count)
