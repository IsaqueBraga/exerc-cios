nome = input("Digite o nome do cliente: ")
dia = int(input("Digite o dia de vencimento: "))
mes = (input("Digite o mês de vencimento: "))
valor = float(input("Digite o valor da fatura: "))
print("Olá,", nome)
print("A sua fatura com vencimento em {} de {} no valor de R${:.0f},00 está fechada.".format(dia, mes , valor))