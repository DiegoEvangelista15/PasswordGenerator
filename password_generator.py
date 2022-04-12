import json
from tkinter import *
from tkinter import messagebox
import string
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    input3.delete(0, END)
    letras = string.ascii_letters
    points = string.punctuation
    numbers = '0123456789'
    tudo = letras + points + numbers

    password_new = ''.join(random.sample(tudo, 10))

    input3.insert(0, password_new)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = input.get()
    email = input2.get()
    password = input3.get()
    new_data = {web: {
        'email': email,
        'password': password,
    }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title='Erro', message='Voce precisa preencher os campos em branco')
    else:

        itsok = messagebox.askokcancel(title='Website',
                                       message=f'Segue os detalhes do seus dados:\nWeb: {web}\nEmail: {email}\n'
                                               f'Senha: {password}\nDeseja salvar os dados?')
        messagebox.showinfo(title='Mensagem', message='Arquivo Salvo!!')

        if itsok:
            try:
                with open('data.json', 'r') as data_file:
                    # json.dump(new_data, data_file, indent=4)
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                input.delete(0, END)
                input3.delete(0, END)

        else:
            messagebox.showinfo(title='Mensagem', message='Nada foi salvo, Obrigado!!')
            input.delete(0, END)
            input3.delete(0, END)


def find_password():
    web = input.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message=f'Nao foram inseridos dados!!!')
    else:
        if len(web) == 0:
            messagebox.showinfo(title='Error', message=f'Nao foram inseridos dados')
        elif web in data:
            m_email = data[web]['email']
            m_password = data[web]["password"]
            messagebox.showinfo(title=web, message=f'Os dados sao:\nEmail:{m_email}\nPassword:{m_password}')
        else:
            messagebox.showinfo(title='Error', message=f'Nao existe os dados de {web} no arquivo Json')


# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title('Password Generator')
windows.config(pady=50, padx=50)

website = Label(text='Website')
website.grid(column=0, row=1)

email_username = Label(text='Email/Username')
email_username.grid(column=0, row=2)

password = Label(text='Password')
password.grid(column=0, row=3)

input = Entry(width=36)
input.grid(column=1, row=1)
input.focus()

input2 = Entry(width=55)
input2.grid(column=1, row=2, columnspan=2)
input2.insert(0, 'Diego@email.com ')

input3 = Entry(width=36)
input3.grid(column=1, row=3)

button_generate_pass = Button(text='Search', width=14, command=find_password)
button_generate_pass.grid(column=2, row=1)

button_generate_pass = Button(text='Generate Password', command=generate_pass)
button_generate_pass.grid(column=2, row=3)

button_add = Button(text='Add', width=30, command=save_password)
button_add.grid(column=1, row=4, columnspan=1)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

windows.mainloop()
