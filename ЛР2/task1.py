salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
salary_vsego = salary
spend_vsego = spend
for i in range(months-1):
    salary_vsego += salary
    spend = spend*(increase+1)
    spend_vsego += spend
money_capital = spend_vsego-salary_vsego
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
