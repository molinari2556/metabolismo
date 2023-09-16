
import tkinter as tk
from tkinter import messagebox


def calculate_metabolism():
    nome = nome_entry.get()
    sexo = sexo_var.get()
    kilos = int(kilos_entry.get())
    altura = int(altura_entry.get())
    idade = int(idade_entry.get())

    if sexo == 'M':
        calculo_homem = 66 + (13.8 * kilos) + (5 * altura) - (6.8 * idade)
        perder_peso_homem = calculo_homem - 500
        ganhar_peso_homem = calculo_homem + 500
        result_label.config(text=f'Seu Metabolismo basal é de {calculo_homem:.2f} calorias')
        result2_label.config(text=f'Para perder peso consuma {perder_peso_homem:.2f}')
        result3_label.config(
            text=f'Para manter seu peso consuma {calculo_homem:.2f} (considerando sem atividade física)')
        result4_label.config(text=f'Para ganhar peso consuma {ganhar_peso_homem:.2f}')
    elif sexo == 'F':
        calculo_mulher = 655 + (9.6 * kilos) + (1.8 * altura) - (4.7 * idade)
        perder_peso_mulher = calculo_mulher - 300
        ganhar_peso_mulher = calculo_mulher + 300
        result_label.config(text=f'Seu Metabolismo basal é de {calculo_mulher:.2f} calorias')
        result2_label.config(text=f'Para perder peso consuma {perder_peso_mulher:.2f}')
        result3_label.config(
            text=f'Para manter seu peso consuma {calculo_mulher:.2f} (considerando sem atividade física)')
        result4_label.config(text=f'Para ganhar peso consuma {ganhar_peso_mulher:.2f}')
    else:
        messagebox.showerror('Erro', 'Você precisa selecionar o sexo corretamente.')


app = tk.Tk()
app.geometry('500x400')
app.title('Calculadora de Metabowlismo Basal')

nome_label = tk.Label(app, text='Nome:')
nome_label.pack()
nome_entry = tk.Entry(app)
nome_entry.pack()

sexo_label = tk.Label(app, text='Sexo:')
sexo_label.pack()
sexo_var = tk.StringVar()
sexo_var.set('M')
sexo_radiobutton1 = tk.Radiobutton(app, text='Masculino', variable=sexo_var, value='M')
sexo_radiobutton2 = tk.Radiobutton(app, text='Feminino', variable=sexo_var, value='F')
sexo_radiobutton1.pack()
sexo_radiobutton2.pack()

kilos_label = tk.Label(app, text='Peso (kg):')
kilos_label.pack()
kilos_entry = tk.Entry(app)
kilos_entry.pack()

altura_label = tk.Label(app, text='Altura (cm):')
altura_label.pack()
altura_entry = tk.Entry(app)
altura_entry.pack()

idade_label = tk.Label(app, text='Idade:')
idade_label.pack()
idade_entry = tk.Entry(app)
idade_entry.pack()

calculate_button = tk.Button(app, text='Calcular', command=calculate_metabolism)
calculate_button.pack()

result_label = tk.Label(app, text='', font=('Helvetica', 12, 'bold'))
result_label.pack()
result2_label = tk.Label(app, text='')
result2_label.pack()
result3_label = tk.Label(app, text='')
result3_label.pack()
result4_label = tk.Label(app, text='')
result4_label.pack()

app.mainloop()