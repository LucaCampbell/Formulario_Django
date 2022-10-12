def origem_destino_iguais(origem, destino, lista_erros):
    '''Verifica se origem e destino são iguais'''
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_erros):
    '''Verifica se tem algum número no campo de formulário'''
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Não inclua números neste campo'


def data_ida_maior_que_data_volta(data_ida, data_volta, lista_erros):
    '''Verifica se data de ida é maior que a data de volta'''
    if data_ida > data_volta:
        lista_erros['data_volta'] = 'Data de volta não pode ser menor que a data de ida'

def data_ida_menor_que_dia_atual(data_ida, data_pesquisa, lista_erros):
    '''Verifica se a data de ida é maior que o dia da pesquisa'''
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = 'Você perdeu o vôo'