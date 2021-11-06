sal = float(input('Digite seu salário: '))
if 0 < sal <= 1765.25:
    aum_01 = sal + (sal * 7.5 / 100)
elif 1766.26 < sal <= 2985.99:
    aum_01 = sal + (sal * 9 / 100)
elif 2986.00 < sal <= 3568.99:
    aum_01 = sal + (sal * 11 / 100)
else:
    aum_01 = sal + (sal * 13 / 100)
print(f"Seu novo salário é de R${aum_01} reais")
