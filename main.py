import time
import os
from Investimetos import invetimento


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
investimentos = []


def investimento_menu():

    bool_deposito_recorente
    esperando = True
    percentual = float(input(f"Qual o percentual?({cor_azul}% do CDI{reset}) "))
    aporte = float(input(f"Qual é o {cor_azul}valor{reset} do aporte de entrada? "))

    while esperando:

        deposito_recorente = input(f"Serão depósitados mensalmente recorrentes?({cor_azul}sim/não{reset}) ").upper()

        if deposito_recorente == "SIM":
            bool_deposito_recorente = True
            esperando = False
        elif deposito_recorente == "NÂO" or deposito_recorente == "NAO" :
            bool_deposito_recorente = False
            esperando = False
        else:
            print(f"{italico}Digite ({cor_azul}sim/não{reset})")
            esperando = True

        
    investimentos.append(invetimento(percentual = percentual, aporte_inicial = aporte, recorrente = bool_deposito_recorente ))
    print(f"{italico}Investimento adicionado com sucesso!!!{reset}")

def menu():
    opcao = input(f"\nDigite {cor_azul}[novo]{reset} investimento, {cor_azul}[sair]{reset} ou aperte {cor_azul}[enter]{reset} para avançar em um mês: ").lower()

    if opcao == "sair":
        print("\nObrigado por usar o simulador. Até logo!")
        condicao = False

    elif opcao == "novo":
        print("\nIniciando cadastro de um novo investimento...")
        investimento_menu()
        time.sleep(1.0)

    elif opcao == "":
        print("\nAvançando um mês...")
        time.sleep(1.0)

    else:
        print("\nOpção inválida! Por favor, digite 'novo', 'sair' ou pressione 'enter' para continuar.")  
        time.sleep(1.0)


while condicao: 
    os.system('cls' if os.name == 'nt' else 'clear')

    print("[SIMULADOR DE INVESTIMENTOS RECORRENTES]\n")
    time.sleep(0.5)
    print(f"\n{italico}Bem vindo, vamos simular também investimentos recorrentes!{reset}")
    print(f"{italico}Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez{reset}\n")
    time.sleep(1.0)

    print(f"\n{italico}Iniciando as simulações...{reset}")
    time.sleep(1.5)

    #Interface do menu 
    menu()
