#Multiplas Funcões--Exercício Controle de Qualidade--
def cabecalho():
    print("\n "+"="*30)
    print("SISTEMA DE QUALIDADE")
def verificar_status(peso):
    if peso >= 50 and peso <= 100:
       return "Aprovada"
    else:
        return "Reprovado"
cabecalho()
peso_item = float(input("Digite o Peso do Item em Gramas:"))
status = verificar_status(peso_item)
print(f"Resultado da Inpeção:{status}")
print("="*30)   