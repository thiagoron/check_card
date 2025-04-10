def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão de crédito com base no número do cartão.
    
    Args:
        numero_cartao (str): Número do cartão de crédito como string.
    
    Returns:
        str: Nome da bandeira ou 'Desconhecida' se não for possível identificar.
    """
    numero_cartao = numero_cartao.replace(" ", "").replace("-", "")
    
    if numero_cartao.isdigit():
        if numero_cartao.startswith("4") and len(numero_cartao) in [13, 16, 19]:
            return "Visa"
        elif numero_cartao.startswith(("51", "52", "53", "54", "55")) and len(numero_cartao) == 16:
            return "MasterCard"
        elif numero_cartao.startswith("34") or numero_cartao.startswith("37") and len(numero_cartao) == 15:
            return "American Express"
        elif numero_cartao.startswith("6011") or numero_cartao.startswith(("622", "64", "65")) and len(numero_cartao) == 16:
            return "Discover"
        elif numero_cartao.startswith("35") and len(numero_cartao) == 16:
            return "JCB"
        elif numero_cartao.startswith("36") or numero_cartao.startswith("38") and len(numero_cartao) == 14:
            return "Diners Club"
        else:
            return "Desconhecida"
    else:
        return "Número inválido"

# Exemplo de uso
numero = input("Digite o número do cartão de crédito: ")
bandeira = identificar_bandeira(numero)
print(f"Bandeira identificada: {bandeira}")