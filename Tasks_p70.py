name = input("Привет. Как тебя зовут?")
age = input("Сколько тебе лет?")
age = int(age)
seconds = age * 365 * 24 * 60 * 60
print("\nТвой нынешний возраст - свыше", seconds, "секунд.")