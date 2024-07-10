menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
 """

saldo = 0
limite = 500
numero_saque= 0
LIMITE_SAQUES=3
extrato =""
while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depositar")
        deposito = float (input("Qual valor deseja depoistar?" ))
        if deposito > 0:
            saldo = saldo + deposito
            extrato += f"Deposito: RS {deposito:.2f}\n"
            print(f"Você acabou de depositar R$ {deposito:.2f}\n")
        else:
            print("Você digitou um valor inválido!")


    elif opcao == "2":
        print("Sacar")
        saque = float(input("Digite o valor que deseja sacar " ))
        if numero_saque<=3:
            if saque<=500 and saque>0:
                if saque <=saldo:
                    saldo = saldo - saque
                    numero_saque=numero_saque+1
                    print(f"Saque de R$ {saque:.2f}")
                    extrato += f"Saque: RS{saque:.2f}\n"

                else:
                    print("Erro!O valor do saque é maior que o valor do saldo!") 
            else:
                    print("Excedeu o valor limite do saque!")
        else:
            print("Excedeu a quantidade limite de saque diário!")
    
    elif opcao == "3":
        print("\n-------------EXTRATO--------------")
        print("Não foram realizadas monimentações" if not extrato else extrato)
        print(f"Extrato da conta R${saldo:.2f}\n")
        print("\n----------------------------------")
    
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por avor selecione novamente a opção desejada")