# Câu 04: Tìm các số chia hết cho 7 nhưng không chia hết cho 5
result = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))
print(",".join(result))


