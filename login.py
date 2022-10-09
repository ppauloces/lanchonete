import PySimpleGUI as sg
import conn as con


def login_screen():

    sg.theme('SandyBeach')
    sg.set_options(font=('Courier 16'),text_color = 'black')

    layout = [
        [sg.Text("Login")],
        [sg.Text("User"),sg.Push(),sg.Input(key='name')],
        [sg.Text("Pass"),sg.Push(),sg.Input(key='pass')],
        [sg.Button("ENTER",expand_x=True)]
    ]
    window = sg.Window("Login",layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        
        if event == 'ENTER':
            name = values['name']
            passw = values['pass']
        if name == '' or passw == '':
            sg.Popup('Os campos não podem ser vazios')
        else:

            cursor = con.conn().cursor()

            comando = 'SELECT * FROM adm WHERE nome = "Paulo"'

            cursor.execute(comando)
 
            resultado = cursor.fetchall() # ler o banco de dados

            if len(resultado) >= 1:

                lista = "A informação foi adicionada na base de dados"
                choice = sg.PopupOKCancel(lista, "Por favor, confirme sua entrada")

                if choice == 'OK':
                    sg.PopupQuick('Login realizado com sucesso')

                    cursor.close()
                    con.close()
                    print("A conexão ao MYSQL foi encerrada")
                    
                    window.close()
            else: 
                sg.Popup("Algo de errado não está certo...")
