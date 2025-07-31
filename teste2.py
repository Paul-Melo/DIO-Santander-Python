# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()


# TODO: Aplique o desconto se o cupom for válido:

desconto = descontos.get(cupom, 0.00)

if preco > 0:
    valor_com_desconto = preco * (1 - desconto)
    print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
else:
    print("Operação falhou! O cupom informado é inválido.")