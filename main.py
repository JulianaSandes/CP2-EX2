from funcoes import calcular_imposto, estado_valido

def main():
    while True:
        # Solicita o valor da venda e o estado ao qual a venda se destina
        try:
            valor = float(input("Digite o valor total da venda: "))
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
            continue

        estado = input("Digite a sigla do estado (AM, MG, RJ, SP, MS): ").upper()

        # Verifica se o estado é válido
        if estado_valido(estado):
            valor_com_imposto = calcular_imposto(valor, estado)
            print(f"Valor final com imposto para {estado}: R$ {valor_com_imposto:.2f}")
            
        elif estado not in ["AM", "MG", "RJ", "SP", "MS"]:
            print(f"A empresa não comercializa produtos no estado {estado}.")
            
        else:
            print("Estado inválido.")

        # Pergunta ao usuário se deseja continuar ou sair
        continuar = input("Deseja fazer outra consulta? (Sim,Não): ").lower()
        if continuar != 'sim':
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    main()
