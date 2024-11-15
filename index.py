print(f'------Desafio Classificador de Nivél de Herói------')


nome = input("Qual o nome do seu Herói? ")
quantidadeXp = int(input("Qual sua quantidade de xp?"))
nivel = ""

if quantidadeXp < 1000:
    nivel = "Ferro"
elif quantidadeXp >= 1001 and quantidadeXp <= 2000:
    nivel = "Bronze"  
elif quantidadeXp >= 2001 and quantidadeXp <= 5000:
    nivel = "Prata"  
elif quantidadeXp >= 5001 and quantidadeXp <= 7000:
    nivel = "Ouro"  
elif quantidadeXp >= 7001 and quantidadeXp <= 8000:
    nivel = "Platina"  
elif quantidadeXp >= 8001 and quantidadeXp <= 9000:
    nivel = "Ascendete"  
elif quantidadeXp >= 9001 and quantidadeXp <= 10000:
    nivel = "Imortal"  
elif quantidadeXp >= 10001:
    nivel = "Radiante"  

print(f"O Herói de nome {nome} está no nível de {nivel}")
     