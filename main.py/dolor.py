import matplotlib.pyplot as plt
import random

random_numbers = [random.randint(1, 100) for _ in range(7)]
rundunt_rg = [random.randint(1, 100) for _ in range(7)]
plt.figure(figsize=(8, 6))
plt.plot(range(1, 8), random_numbers, marker='o', color='b', linestyle='--')
plt.plot(range(1, 8),rundunt_rg, marker='s', color='r', linestyle='--')
plt.title('График случайных чисел')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.grid(True)
plt.show()