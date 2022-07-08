from indetificacaoDefuncoes import *

minhaLista=[]
print("Preenchendo")
preencherinventario(minhaLista)
print("Exibindo")
exibirinventario(minhaLista)
###
###
print("Pesquisando")
localozarpornome(minhaLista)
print("Alterando")
depreciarpornome(minhaLista,  20)
###
###
print("Excluindo")
print(excluirPorSerial (minhaLista))
exibirinventario(minhaLista)
####

print("Resumindo")
resumirValores(minhaLista)


