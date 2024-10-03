taxas_imposto = {
    "AM": 0.17,
    "MG": 0.15,
    "RJ": 0.06,
    "SP": 0.08,
    "MS": 0.12
}

def calcular_imposto(valor, estado):
    """
    Calcula o valor final do produto com imposto baseado no estado.
    """
    if estado in taxas_imposto:
        taxa = taxas_imposto[estado]
        valor_final = valor * (1 + taxa)
        return valor_final
    else:
        return None

def estado_valido(estado):
    """
    Verifica se o estado digitado está na lista dos que a empresa comercializa.
    """
    if estado in taxas_imposto:
        return True
    else:
        return False
