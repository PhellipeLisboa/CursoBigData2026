# Aula 02 - Dia 14/08/2026
# Tema principal: Condicionais

# x = 100
# y = 99.9
# print("x é maior que y?", x > y)
# print("x é igual a y?", x == y)

# resposta = x>y
# print(resposta)
# print(type(resposta))

# tem_carteira = True
# idade = 18
# tem_carro = False
# pode_dirigir = idade >= 18 and tem_carteira
# print("Pode dirigir?", pode_dirigir)
# print("Pode dirigir e tem carro?", pode_dirigir and tem_carro)

# frase = "Python é divertido"
# print(frase.upper())
# nova_frase = frase.replace("divertido", "poderoso")
# print(nova_frase)

# EXEMPLO 1
# cnh = True
# bebidinha = False

# posso_dirigir = cnh and not bebidinha
# print(posso_dirigir)

# EXEMPLO 2
# busaum = False
# trenzin = False

# venho_para_aula = busaum or trenzin
# print(venho_para_aula)

# EXEMPLO 3

locomocao = input("Informe sua locomoção: ")
choveu = True

if choveu and locomocao == 'moto':
    resultado = "Tô todo molhado :("
elif not choveu and locomocao == 'moto':
    resultado = "Tô seco :)"
else:
    resultado = "Tô seco :)"

print(resultado)