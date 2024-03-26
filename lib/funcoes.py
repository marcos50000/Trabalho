from database import Jogador, Time

jogadores = []
times = []

def cadastrar_jogador(nome, idade, posicao, time):
    jogador = Jogador(nome, idade, posicao, time)
    jogadores.append(jogador)

def listar_jogadores():
    for jogador in jogadores:
        print(f"Nome: {jogador.nome}, Idade: {jogador.idade}, Posição: {jogador.posicao}, Time: {jogador.time}")

def consultar_jogador(nome):
    for jogador in jogadores:
        if jogador.nome == nome:
            return jogador
    return None

def apagar_jogador(nome):
    for jogador in jogadores:
        if jogador.nome == nome:
            jogadores.remove(jogador)

def atualizar_jogador(nome, idade, posicao, time):
    for jogador in jogadores:
        if jogador.nome == nome:
            jogador.idade = idade
            jogador.posicao = posicao
            jogador.time = time

def cadastrar_time(nome, cidade):
    time = Time(nome, cidade)
    times.append(time)

def listar_times():
    for time in times:
        print(f"Nome: {time.nome}, Cidade: {time.cidade}")

def consultar_time(nome):
    for time in times:
        if time.nome == nome:
            return time
    return None

def apagar_time(nome):
    for time in times:
        if time.nome == nome:
            times.remove(time)

def atualizar_time(nome, cidade):
    for time in times:
        if time.nome == nome:
            time.cidade = cidade