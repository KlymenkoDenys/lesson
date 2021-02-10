# Расчет стоимости автомобиля

cost = int(input("Стоимость авто: "))

tax = cost * 0.2                    # Налог на машину
registration = cost * 0.3           # Регистрация автомобиля
agent = 1000                        # Услуги агента
delivery = 2000                     # Доставка автомобиля
total = cost + tax + registration + agent + delivery    # Общая стоимость автомобиля

print("Общая стоимость авто", total, "uah")
print(f"Общая 'hi' стоимость авто {total} uah", f"налог равен {tax}")

input("Нажмите Enter, чтобы выйти: ")
