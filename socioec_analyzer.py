from csv import reader

terceiro = segundo = primeiro = contagem = aut = edf = adm = 0


def count_grade(line):
    """
    Conta os estudantes de cada ano e curso
    """
    global primeiro, segundo, terceiro, aut, edf, adm
    if line[3] == "Terceiro Ano":
        terceiro += 1
    if line[3] == "Segundo Ano":
        segundo += 1
    if line[3] == "Primeiro Ano":
        primeiro += 1

    if line[4] == "Automação Industrial":
        aut += 1
    if line[4] == "Edificações":
        edf += 1
    if line[4] == "Administração":
        adm += 1


with open(r"path_to_the_.csv_file") as arquivo:
    dados = reader(arquivo)
    next(dados)
    for linha in dados:
        contagem += 1
        count_grade(linha)
