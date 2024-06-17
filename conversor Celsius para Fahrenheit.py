import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def mostrar_resultado():
    try:
        celsius = float(entry_celsius.get())
        if 0 <= celsius <= 30:
            fahrenheit = converter_celsius_para_fahrenheit(celsius)
            
            # Criar janela
            janela = tk.Tk()
            janela.title("Conversão de Celsius para Fahrenheit")
            
            # Adicionar widgets
            label_celsius = ttk.Label(janela, text="Temperatura em Celsius: " + str(celsius) + "°C")
            label_celsius.pack()
            
            label_fahrenheit = ttk.Label(janela, text="Temperatura em Fahrenheit: " + str(fahrenheit) + "°F")
            label_fahrenheit.pack()
            
            # Exibir janela
            janela.mainloop()
        else:
            messagebox.showerror("Erro", "A temperatura deve estar entre 0 e 30 graus Celsius.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

# Criar janela principal
root = tk.Tk()
root.title("Conversor de Temperatura")

# Adicionar widgets
label_instrucao = ttk.Label(root, text="Digite a temperatura em Celsius (até 30):")
label_instrucao.pack()

entry_celsius = ttk.Entry(root)
entry_celsius.pack()

botao_converter = ttk.Button(root, text="Converter", command=mostrar_resultado)
botao_converter.pack()

# Exibir janela principal
root.mainloop()
