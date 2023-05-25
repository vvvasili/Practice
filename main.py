per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("введите сумму"))
deposit = [per_cent[i] * money / 100 for i in per_cent]
print(deposit)
max_deposit = deposit[0]
for deposit in deposit:
    if deposit > max_deposit:
        max_deposit = deposit
print("Максимальная сумма, которую вы можете заработать" + str(max_deposit))

