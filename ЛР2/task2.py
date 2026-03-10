money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
summa = salary + money_capital
mes = 0
while summa > spend:
    mes +=1
    summa = summa - spend
    spend +=spend*increase
    summa+=salary
print("Количество месяцев, которое можно протянуть без долгов:", mes)
