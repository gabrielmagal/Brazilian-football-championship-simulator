from random import randint

def Exercicios():
    print("━━━━━━━━━━━━━━━✦✗✦━━━━━━━━━━━━━━━━")
    print(" █▀▀█ █░░▒█ ▀▀█▀▀ █░▒█ █▀▀▀█ █▄░▒█ ")
    print(" █▄▄█ █▄▄▄█ ░▒█░░ █▀▀█ █░░▒█ █▒█▒█ ")
    print(" █░░░ ░▒█░░ ░▒█░░ █░▒█ █▄▄▄█ █░░▀█ ")
    print("━━━━━━━━━━━━━━━✦✗✦━━━━━━━━━━━━━━━━")

## Essa ordem de '0' segue por: Vitórias, Derrotas, Empates, Gols marcados, Gols Sofridos e Pontos do campeonato
##Aqui tem todos os times participantes do Campeonato Brasileiro
times = [["Internacional", 0, 0, 0, 0, 0, 0],
        ["São Paulo", 0, 0, 0, 0, 0, 0],
        ["Vasco da Gama", 0, 0, 0, 0, 0, 0],
        ["Fluminense", 0, 0, 0, 0, 0, 0],
        ["Atlético-MG", 0, 0, 0, 0, 0, 0],
        ["Palmeiras", 0, 0, 0, 0, 0, 0],
        ["Fortaleza", 0, 0, 0, 0, 0, 0],
        ["Bahia", 0, 0, 0, 0, 0, 0],
        ["Flamengo", 0, 0, 0, 0, 0, 0],
        ["Santos", 0, 0, 0, 0, 0, 0],
        ["Ceará SC", 0, 0, 0, 0, 0, 0],
        ["Grêmio", 0, 0, 0, 0, 0, 0],
        ["Athletico-PR", 0, 0, 0, 0, 0, 0],
        ["Coritiba", 0, 0, 0, 0, 0, 0],
        ["Botafogo", 0, 0, 0, 0, 0, 0],
        ["Corinthians", 0, 0, 0, 0, 0, 0],
        ["Bragantino-SP", 0, 0, 0, 0, 0, 0],
        ["Goiás", 0, 0, 0, 0, 0, 0],
        ["Sport Recife", 0, 0, 0, 0, 0, 0],
        ["Atlético-GO", 0, 0, 0, 0, 0, 0]]



for i in range(0, times.__len__()):
    for j in range(0, times.__len__()): ## um for dentro de outro for para ter um loop entre todos os times 2x
        if i != j: ## Aqui eu estou anulando a possíbilidade do time jogar com ele mesmo...
            time1 = randint(0, 5) ## Fazer um valor de gols randomico para o time1
            time2 = randint(0, 5)  ## Fazer um valor de gols randomico para o time2
            if time1 == time2: ## Comparar para ver se os times contem a mesma quantia de gols para empatar
                times[i][3] += 1 ## Caso tenham, acrescento 1 na tabela do empate
                times[j][3] += 1 ## acrescento 1 também para o adversário
                times[i][6] += 1 ## Aqui acrescento aos pontos dele +1 pois empate vale 1
                times[j][6] += 1 ## Aqui acrescento aos pontos do adversário +1 pois empate vale 1
                print("Empate - {} {}x{} {}".format(times[i][0], time1, time2, times[j][0])) ## Exemplo de saída: "Empate - Atlético-GO 5x5 Botafogo"

            if time1 > time2: ## Caso o Time 1 vença em gols

                #############Ganhador#############
                times[i][1] += 1 ## +1 vitória
                times[i][4] += time1 ## Gols marcados
                times[i][5] += time2  ## Gols Sofridos
                times[i][6] += 3  ## +3 Pontos como na tabela
                ###################################

                #############Perdedor#############
                times[j][2] += 1 ## +1 Derrota
                times[j][4] += time2  ## Gols marcados
                times[j][5] += time1 ## Gols que tomou
                #############Perdedor#############

                print("{} {}x{} {}".format(times[i][0], time1, time2, times[j][0])) ## Placar de vencedor, Exemplo de saída: "Atlético-GO 4x1 Sport Recife"

            if time1 < time2: ## Caso o Time 2 vença em gols
                #############Ganhador#############
                times[j][1] += 1  ## Vitória
                times[j][4] += time2  ## Gols que marcou
                times[j][5] += time1  ## Gols Sofridos
                times[j][6] += 3  ## +3 Pontos como na tabela
                ###################################

                #############Perdedor#############
                times[i][2] += 1  ## +1 Derrota
                times[i][4] += time1  ## Gols marcados
                times[i][5] += time2  ## Gols que tomou
                ###################################

                print("{} {}x{} {}".format(times[j][0], time2, time1, times[i][0])) ## Placar de vencedor, Exemplo de saída: "Atlético-GO 4x1 Sport Recife"


print("\n\n") ## Quebra de linhas apenas para ficar mais vísivel o resultado

for i in range(0, times.__len__()): ## Agora eu mostro quais são os dados do campeonato em sí.
    print("{}, Pontos: {}, Vitórias: {}, Derrotas: {}, Empates: {}, Gols Feitos : {}, Gols Sofridos : {}".format(times[i][0], times[i][6], times[i][1], times[i][2], times[i][3], times[i][4], times[i][5]))

ganhador = [0, 0]

for i in range(0, times.__len__()):
    if ganhador[0] < times[i][6]:
        ganhador[0] = times[i][6]
        ganhador[1] = i

print("\n\n") ## Quebra de linhas apenas para ficar mais vísivel o resultado

print("Hoje apresentamos o " + times[ganhador[1]][0] + " como vencedor do campeonato brasileiro de 2022 " +
      "com um total de " + str(times[ganhador[1]][6]) + " pontos.")
