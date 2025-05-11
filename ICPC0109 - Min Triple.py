import sys

# Đọc input từ stdin
input = sys.stdin.read
data = input().split()
index = 0

T = int(data[index])
index += 1

results = []
for _ in range(T):
    N = int(data[index])
    index += 1
    A = [int(data[index + i]) for i in range(N)]
    index += N
    
    # Tìm tổng nhỏ nhất của bộ ba
    min_sum = float('inf')  # Khởi tạo giá trị vô cực
    for i in range(N):
        for j in range(i + 1, N):
            # Tìm số nhỏ nhất trong các phần tử còn lại
            for k in range(N):
                if k != i and k != j:
                    current_sum = A[i] + A[j] + A[k]
                    min_sum = min(min_sum, current_sum)
    
    results.append(min_sum)

# In kết quả
for result in results:
    print(result)