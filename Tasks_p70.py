name = input("Привет. Как тебя зовут?")
age = input("Сколько тебе лет?")
age = int(age)
weight = int(input("Сколько в тебе килограммов?"))
seconds = age * 365 * 24 * 60 * 60
print("\nТвой нынешний возраст - свыше", seconds, "секунд.")
moon_weight = weight / 6
print("\nЗнаете ли вы, что на Луне вы весили всего", moon_weight, "кг?")
sun_weight = weight * 27.1
print("А вот находясь на Солнце, вы бы весили", sun_weight, "кг, (Но увы, это бы продолжалось не долго..)")
print("\nНажмите Enter, чтобы выйти")
