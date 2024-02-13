# 1G1 - Um restaurante cobra R$28,00 por refeição mais os 10% de taxa serviços, porém
# oferece bonificações para contas caso:

#  - O número de refeições na mesa for de 2 até 4 pessoas a refeição passa a custar R$ 25,00
# e a taxa de serviços é de 7% sobre o valor da conta;
#  - O número de refeições na mesa for de 5 até 8 pessoas a refeição passa a custar R$
# 22,00 e a taxa de serviços é de 5% sobre o valor da conta;
#  - O número de refeições na mesa for acima de 8 pessoas a refeição passa a custar R$
# 20,00 e a taxa de serviços é isenta;

# Faça um programa que calcule o valor da conta de uma mesa quando informado o número de
# pessoas (desconsidere o consume de bebidas e sobremesa)

refeicao = 28.0
taxa = 0.10
numRef = int(input("Digite o número de pessoas\n"))

if numRef < 2:
	refeicao = 28.0
elif numRef <= 4:
	refeicao = 25.0
	taxa = 0.07
elif numRef <= 8:
	refeicao = 22.0
	taxa = 0.05
else:
	refeicao = 20.0
	taxa = 0

conta = (numRef * refeicao) * (1 + taxa)

# print(f"Valor da conta: {conta}")
print("Valor da conta: %.2f" %conta)
