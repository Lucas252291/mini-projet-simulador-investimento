import time
import os

cor_vermelho = "\033[31m"
cor_verde = "\033[32m"
cor_azul = "\033[34m"
cor_amarelo = "\033[33m"
cor_roxo = "\033[35m"
cor_ciano = "\033[36m"
cor_branco = "\033[37m"
italico = "\033[3m"
negativo = "\033[7m"
reset = "\033[0m"
linha_anterior = "\033[F"
cima_da_linha = "\033[A"

condicao = True 

while condicao: 
    os.system('cls' if os.name == 'nt' else 'clear')

    print("[SIMULADOR DE INVESTIMENTOS RECORRENTES]\n")
    time.sleep(0.5)
    print(f"\n{italico}Bem vindo, vamos simular também investimentos recorrentes!{reset}")
    print(f"{italico}Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez{reset}\n")
    time.sleep(1.0)

    print(f"\n{italico}Iniciando as simulações...{reset}")
    time.sleep(1.5)

    opcao = input(f"\nDigite {cor_azul}[novo]{reset} investimento, {cor_azul}[sair]{reset} ou aperte {cor_azul}[enter]{reset} para avançar em um mês: ").lower()

    if opcao == "sair":
        print("\nObrigado por usar o simulador. Até logo!")
        condicao = False

    elif opcao == "novo":
        print("\nIniciando cadastro de um novo investimento...")
        time.sleep(1.0)

    elif opcao == "":
        print("\nAvançando um mês...")
        time.sleep(1.0)

    else:
        print("\nOpção inválida! Por favor, digite 'novo', 'sair' ou pressione 'enter' para continuar.")  
        time.sleep(1.0)        
