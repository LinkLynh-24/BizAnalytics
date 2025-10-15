#
# Linh
# Print Hello World!
#

# 1. Input

# 2. Process

# 3. Output
# print('Hello THU!')
# print("I like Professor Kim's class")

# print("Output:", end=" ")
# for i in range(1, 6):
#     if i < 5:
#         # print(f"Count: {i}", end=', ')
#     else:
#         # print(f"Count: {i}")
    
orderValues = [120, 450, 80, 300, 650]
total = 0
count = 0
for order in orderValues:
    total += order
    count += 1
    print(f"processing order: {order}")

print(f"total revenue: {total}")
print(f"total items: {count}")