from time import sleep #Importa Função "Sleep" da Biblioteca de Tempo

nomes = [] #Lista de Nomes
notas = [] #Lista de Notas

print("--- CALCULADORA DE NOTAS ---")

#Adiciona os Alunos e Suas Respectivas Notas
while True:
    nome = str(input("Nome: ")).strip().capitalize() #Nome do Aluno
    nota_2 = float(input("Nota 1: ")) #1ª Nota do Aluno
    nota_1 = float(input("Nota 2: ")) #2ª Nota do Aluno

    nomes.append([nome]) #Adiciona 'Nome' à lista 'Nomes'
    notas.append([nota_1, nota_2]) #Adiciona 'Nota 1' e 'Nota 2' à lista 'Notas'

    sleep(0.5)
    continuar = str(input("\nQuer continuar? [S/n] ")).strip().upper() #Para ou Continua o Loop de Acordo com a Escolha do Usuário
    if continuar == "S":
        continue
    elif continuar == "N":
        break

#Dados dos Alunos
def dados():
    sleep(0.5)
    print(f"\n{'Num:':<8}{'Nome:':<14}{'Nota Média:':>10}")
    print("================================")

    for posicao, aluno in enumerate(nomes):
        media_notas = sum(notas[posicao]) / 2 #Média das Notas
        print(f"{posicao:<8}{aluno[0]:<14}{media_notas:>10.1f} ")

    print("================================\n")

dados()

#Mostra Notas de um Aluno em Específico
sleep(0.5)
while True:
    aluno_notas = int(input("Mostrar dados de qual aluno? (999 para parar) "))

    sleep(0.5)
    if aluno_notas != 999:
        try:
            print(f"As notas de {nomes[aluno_notas][0]} são: {notas[aluno_notas]}")

            dados()
        except:
            print("Esse aluno não está em nosso banco de dados...")

            sleep(0.5)
            dados()
    elif aluno_notas == 999:
        break

#Fim do Programa
sleep(0.5)
print("Saindo do programa...")
