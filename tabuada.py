numero = int(input("Tabuada de qual número? "))
print(F"--- Tabuada do {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

