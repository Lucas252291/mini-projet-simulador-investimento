import time
import os
from Investimetos import investimento

# Códigos de escape ANSI
cor_vermelho = "\033[31m"; cor_verde = "\033[32m"; cor_azul = "\033[34m"
cor_amarelo = "\033[33m"; cor_roxo = "\033[35m"; cor_ciano = "\033[36m"
cor_branco = "\033[37m"; italico = "\033[3m"; reset = "\033[0m"

investimentos = []
TAXA_CDI_MENSAL = 0.01145 # 1.145% para obter R$2,29 de rendimento em R$200 para 100% CDI

meses_nomes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
indice_mes_atual = 3  # Começa em Abril
ano_atual = 2025

def menu_investimento():
    global investimentos
    
    print(f"\n{italico}Iniciando cadastro de um novo investimento...{reset}")
    deposito_recorrente = False
    esperando_percentual = True
    while esperando_percentual:
        try:
            percentual_str = input(f"Qual o percentual? ({cor_azul}% do CDI{reset}) ")
            percentual = float(percentual_str)
            if percentual <= 0:
                print(f"{cor_vermelho}{italico}O percentual deve ser um número positivo.{reset}")
            else:
                esperando_percentual = False
        except ValueError:
            print(f"{cor_vermelho}{italico}Entrada inválida. Por favor, insira um número para o percentual.{reset}")

    esperando_aporte = True
    while esperando_aporte:
        try:
            aporte_str = input(f"Qual é o {cor_azul}valor{reset} do aporte de entrada? R$")
            aporte = float(aporte_str)
            if aporte <= 0:
                print(f"{cor_vermelho}{italico}O valor do aporte deve ser positivo.{reset}")
            else:
                esperando_aporte = False
        except ValueError:
            print(f"{cor_vermelho}{italico}Entrada inválida. Por favor, insira um número para o aporte.{reset}")

    esperando_recorrente = True
    while esperando_recorrente:
        entrada_deposito_recorrente = input(f"Serão depósitos mensalmente recorrentes? ({cor_azul}sim/não{reset}) ").strip().upper()
        if entrada_deposito_recorrente == "SIM":
            deposito_recorrente = True
            esperando_recorrente = False
        elif entrada_deposito_recorrente == "NÃO" or entrada_deposito_recorrente == "NAO":
            deposito_recorrente = False
            esperando_recorrente = False
        else:
            print(f"{cor_vermelho}{italico}Resposta inválida. Digite {cor_azul}sim{reset} ou {cor_azul}não{reset}.{reset}")

    # Usando argumentos posicionais em vez de nomeados
    novo_investimento = investimento(percentual, aporte, deposito_recorrente)
    
    investimentos.append(novo_investimento)
    print(f"\n{cor_verde}{italico}Investimento adicionado com sucesso!{reset}")
    time.sleep(0.5)


def executar_ciclo_simulacao():
    global indice_mes_atual, ano_atual, investimentos

    if not investimentos: return

    # 1. Calcula o rendimento para o período que acabou de "terminar"
    for inv in investimentos:
        rendimento_do_periodo = inv.valor_atual * inv.percentual * TAXA_CDI_MENSAL
        inv.valor_atual += rendimento_do_periodo
        
    # 2. Avança o mês da simulação
    indice_mes_atual += 1
    if indice_mes_atual == 12:
        indice_mes_atual = 0; ano_atual += 1
    
    # 3. Aplica depósitos recorrentes para o novo mês iniciado
    for inv in investimentos:
        if inv.recorrente:
            inv.total_investido += inv.aporte_inicial
            inv.valor_atual += inv.aporte_inicial


def main():
    global indice_mes_atual, ano_atual

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{cor_ciano}[SIMULADOR DE INVESTIMENTOS RECORRENTES]{reset}\n")
    time.sleep(0.5); print(f"{italico}Bem vindo, vamos simular também investimentos recorrentes!{reset}")
    print(f"{italico}Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez.{reset}\n")
    time.sleep(1.0); print(f"{italico}Iniciando as simulações...{reset}"); time.sleep(1.5)

    continuar = True

    while continuar:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{cor_ciano}[SIMULADOR DE INVESTIMENTOS RECORRENTES]{reset}\n")
        print(f"{cor_amarelo}[SIMULAÇÃO]{reset}\n")

        # Exibe estado atual
        if not investimentos:
            print(f"{italico}Nenhum investimento cadastrado ainda.{reset}")
        else:
            for inv in investimentos:
                prefixo = f"{cor_verde}[R]{reset}" if inv.recorrente else f"{cor_roxo}[U]{reset}"
                print(f"{prefixo} LCI de {inv.percentual * 100:.2f}% do CDI R${inv.total_investido:.2f}, R${inv.valor_atual:.2f}")

        print(f"\n{italico}resumo da simulação em {meses_nomes[indice_mes_atual]} de {ano_atual}{reset}")
        print("---")

        opcao = input(f"\nDigite {cor_azul}[novo]{reset} investimento, {cor_azul}[sair]{reset} ou aperte {cor_azul}[enter]{reset} para avançar em um mês: ").strip().lower()

        if opcao == "sair":
            print("\nObrigado por usar o simulador. Até logo!")
            continuar = False
        elif opcao == "novo":
            menu_investimento()
        elif opcao == "":
            print("\nAvançando um mês...")
            executar_ciclo_simulacao()
            time.sleep(1.0)
        else:
            print(f"\n{cor_vermelho}Opção inválida!{reset} Por favor, digite 'novo', 'sair' ou pressione 'enter'.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()