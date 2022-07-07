inventario=[]
resposta = "S"
while resposta == "S":
    equipamentos=[input(" Equipamentos: "),
                float(input("Valor: ")),
                int(input("Número do serial: ")),
                input("Depaqrtamentos: ")]
    inventario.append(equipamentos)
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
     print("Nome........: ", elemento[0]) 
     print("Valor.......: ", elemento[1]) 
     print("Serial......: ", elemento[2])
     print("Departamento.: ", equipamentos[3]) 

busca=input("\nDigite o nome do equipamento que deseja busacar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("Valor. .:", elemento[1])
        print("Serial. .:", elemento[2]) 

depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in  inventario:
    if depreciacao==elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

serial=input("\nDigite o serial do equipamento que será excluido: ")
for elemento in  inventario:
    if depreciacao==serial[2]:
        inventario.remove(elemento)

for elemento in inventario:
     print("Nome........: ", elemento[0]) 
     print("Valor.......: ", elemento[1]) 
     print("Serial......: ", elemento[2])
     print("Departamento.: ", equipamentos[3]) 

valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print(" Oequipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de : ", sum(valores))     
            

