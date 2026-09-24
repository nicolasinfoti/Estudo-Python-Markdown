# Projeto Exemplo: Calculadora Média do Aluno


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


print("=== Sistema de Notas do Aluno ===")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = calcular_media(n1, n2)

print(f"A média final é: {media:.2f}")

# se for maior ou igual que 7, aluno aprovado.
if media >= 7.0:
    print("Status: APROVADO!")
    
    # se for menor que 7, aluno reprovado.
else:
    print("Status: REPROVADO")
