# Рантье
# Демонстрирует логическую ошибку
print(
    """"
    
                Рантье
    Програма подсчитывает ваши ежемесячные расходы. Эту статистику нужно знать, чтобы
     у вас не закончились деньги и вам не пришлось искать работу.
     Введите сумму расходов по всем статьям, перечисляемые ниже. Вы богаты - так не мелочитесь
     пишите суммы в долларах, без центов.
         """
)
car = int(input("Техническое обслуживание машины 'Лаборгини': "))
rent = int(input("Сьем роскошной квартиры на Манхетене: "))
jet = int(input("Аренда самолета: "))
gifts = int(input("Подарки: "))
food = int(input("Обеды и ужины в ресторанах:"))
staff = int(input("Жалование прислуги: "))
guru = int(input("Плата личному психоаналитику: "))
games = int(input("Компьютерные игры: "))
total = car + rent + jet + gifts + food + staff + guru + games
print("\nОбщая сумма:", total)
input("\n\nНажмите Enter, чтобы выйти.")
