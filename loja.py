print("-=-"*10)
print("SIMULADOR LOJA")
print("-=-"*10)

continuar = ""

valorproduto = float(input("Entre com o valor do produto: R$"))

while(continuar != "N"):
    print("-----Condiçoes de pagamento-----")
    print(
    "[1] - Opção de pagamento a vista\n" ## barra "n", jogar para baixo
    "[2] - Opção de pagamento no cartão\n"
    "[3] - Opção de pagamento em 2x no cartão\n"
    "[4] - Opção de pagamento em 3x no cartão\n"
    )
    cod = int(input("Entre com a condição de pagamento: "))

    if cod == 1:
        valorfinal = valorproduto - valorproduto*10/100 ## valor do produto - 10 porcento dele
    elif cod == 2:
        valorfinal = valorproduto - valorproduto*5/100 ## valor do produto - 5 porcento dele
    elif cod == 3:
        valorfinal = valorfinal = valorproduto
        parcela = valorfinal/2
        print(f"São duas parcelas de R${parcela}")
    elif cod == 4:
            valorfinal = valorproduto + valorproduto*10/100
            parcela = valorfinal/3
            print(f"São três parcelas de R${parcela}")
    else:
        print("Código inválido, digite novamente: ")
        
    if cod in (1,2,3,4):
        print(f"O valor a pagar é R${valorfinal}")
    else:
        print("")
        
    continuar = input("Deseja continuar [S/N]: ").upper()