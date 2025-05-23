# Câu 01: Tính tổng số chẵn trong một list
lst = [1, 2, 3, 4, 5, 6]
even_sum = sum([x for x in lst if x % 2 == 0])
print("Tổng các số chẵn:", even_sum)