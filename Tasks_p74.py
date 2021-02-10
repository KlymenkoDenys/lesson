# Кости
# Демонстрирует генерацию случайных чисел

import random

# Create randome numbers from the range 1 to 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = die1 + die2

print("При вашем броске выпало", die1, "и", die2, "очков, в сумме", total)
input("Нажмите Enter, чтобы выйти.")
