print("Тут вы можете контролировать ваши расходы за неделю")
budget = float(input("Введите ваш начальный бюджет: "))
print("Ваш бюджет: ", budget)
expens1 = float(input("День 1: Сколько вы потратили сегодня? "))
budget -= expens1
print("Остаток бюджета после дня 1: ", budget,"Сом")
expens2 = float(input("День 2: Сколько вы потратили сегодня? "))
budget -= expens2
print("Остаток бюджета после дня 2: ", budget,"Сом")
expens3 = float(input("День 3: Сколько вы потратили сегодня? "))
budget -= expens3
print("Остаток бюджета после дня 3: ", budget,"Сом")
expens4 = float(input("День 4: Сколько вы потратили сегодня? "))
budget -= expens4
print("Остаток бюджета после дня 4 ", budget,"Сом")
expens5 = float(input("День 5: Сколько вы потратили сегодня? "))
budget -= expens5
print("Остаток бюджета после дня 5: ", budget,"Сом")
print(f"После 5 дней ваш остаток бюджета:",budget,("Сом"))

