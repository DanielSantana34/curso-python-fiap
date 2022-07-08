usuarios = {}
print(usuarios)

usuarios = {
   "chaves": ["CHAVES MACONHEIRO", "25/12/2002", "RUA DA LOUCURA"],
    "kiko":  ["kIKO NOIADO", "01/01/2003", "RUA DOS COGUMELOS"]
}
print(usuarios)

usuarios["florinda"] = ["Dona florinda", "12/09/99", "Xícara de café"]
print(usuarios)

print("************")
print(usuarios.get("florinda"))