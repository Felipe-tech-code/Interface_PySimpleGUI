from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')#Definir o tema.
#Cria a estrutura da nossa interface gráfica.
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*')],#O password_char='*' serve para ocultar a senha ao ser digitalizada.
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Entrar':
        if valores['usuario'] == 'Batman' and valores ['senha'] == '123456789':
            print("Seja bem vindo senhor Wayne!")