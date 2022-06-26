nome=input("digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infecciosa=input("Suspeita de doença infecciosa: ")
if idade>=65:
    print("O paciente " + nome + " Possui atendimento prioritário. ") 
elif doenca_infecciosa=="SIM":
    print("O paciente " + nome + " deve ser levado para a sala de espera reservada. ")
else:
    print("O paciente " + nome + " Não possui atendimento prioritário e pode aguardar na sala comum. ")    

