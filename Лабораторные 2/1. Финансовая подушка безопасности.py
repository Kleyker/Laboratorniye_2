money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0 # Первый месяц

while True:
    amount_money = spend - salary # Сумма денег, которая является разностью расходов и зарплаты
    if amount_money > money_capital:
        break

    month += 1
    spend *= (1 + increase) # Затраты увелич. на коэффициент увеличения расходов
    money_capital -= amount_money # Вычитается из подушки разница расходов и зарплаты

print("Количество месяцев, которое можно протянуть без долгов:", month)
