import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import datetime as date

# Tela
root = tk.Tk()
root.title('IDEALIZADOR DE PREÇOS')
root.geometry("750x350")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

style = ttk.Style()
style.configure('TFrame', background='#D9D9D9')

tabControl.add(tab1, text='Idealizador de preços')
tabControl.add(tab2, text='Produtos vendidos')
tabControl.pack(expand=1, fill="both")


def validate_entry(inp):
    if inp == "":
        return True
    try:
        float(inp)
    except:
        return False
    return True

#1
qtd_nom = tk.Label(tab1, text="Quantidade", font='Helvetica 9 bold', background='#D9D9D9')
qtd_inp = tk.Entry(tab1, width=6, validate='key', vcmd=(root.register(validate_entry), '%P'))

nom_nom = tk.Label(tab1, text="Nome", background='#D9D9D9', font='Helvetica 9 bold')
nom_inp = tk.Entry(tab1)

cst_nome = tk.Label(tab1, text="Custo", background='#D9D9D9', font='Helvetica 9 bold')
cst_inp = tk.Entry(tab1, validate='key', vcmd=(root.register(validate_entry), '%P'))

dol_nome = tk.Label(tab1, text="Dolar", background='#D9D9D9', font='Helvetica 9 bold')
dol_inp = tk.Entry(tab1, validate='key', vcmd=(root.register(validate_entry), '%P'))

ml_nome = tk.Label(tab1, text="Tamanho", background='#D9D9D9', font='Helvetica 9 bold')
ml_inp = tk.Entry(tab1, width=7, validate='key', vcmd=(root.register(validate_entry), '%P'))

#1
tabela = ttk.Treeview(tab1, columns=("1", "2", "3", "4", "5", "6", "7", "8", "9"), show="headings")

tabela.column("1", minwidth=0, width=50)
tabela.heading("1", text="Qtd")
tabela.column("2", minwidth=0, width=200)
tabela.heading("2", text="Nome")
tabela.column("3", minwidth=0, width=50)
tabela.heading("3", text="mL")
tabela.column("4", minwidth=0, width=100)
tabela.heading("4", text="Custo total (R$)")
tabela.column("5", minwidth=0, width=60)
tabela.heading("5", text="25%")
tabela.column("6", minwidth=0, width=60)
tabela.heading("6", text="50%")
tabela.column("7", minwidth=0, width=60)
tabela.heading("7", text="100%")
tabela.column("8", minwidth=0, width=60)
tabela.heading("8", text="200%")
tabela.column("9", minwidth=0, width=60)
tabela.heading("9", text="230%")

#1
qtd_nom.grid(column=0, row=0, sticky="w")
qtd_inp.grid(column=0, row=1, sticky="w", padx=10)
nom_nom.grid(column=1, row=0, sticky="w")
nom_inp.grid(column=1, row=1)
cst_nome.grid(column=2, row=0, sticky="w")
cst_inp.grid(column=2, row=1)
dol_nome.grid(column=3, row=0, sticky="w")
dol_inp.grid(column=3, row=1)
ml_nome.grid(column=4, row=0, sticky="w")
ml_inp.grid(column=4, row=1)

tabela.grid(column=0, row=3, columnspan=6, pady=5, padx=10)

#2
qtd_nom2 = tk.Label(tab2, text="Quantidade", font='Helvetica 9 bold', background='#D9D9D9')
qtd_inp2 = tk.Entry(tab2, width=6, validate='key', vcmd=(root.register(validate_entry), '%P'))

nom_nom2 = tk.Label(tab2, text="Nome", background='#D9D9D9', font='Helvetica 9 bold')
nom_inp2 = tk.Entry(tab2)

cst_nome2 = tk.Label(tab2, text="Custo", background='#D9D9D9', font='Helvetica 9 bold')
cst_inp2 = tk.Entry(tab2, validate='key', vcmd=(root.register(validate_entry), '%P'))

dol_nome2 = tk.Label(tab2, text="Dolar", background='#D9D9D9', font='Helvetica 9 bold')
dol_inp2 = tk.Entry(tab2, validate='key', vcmd=(root.register(validate_entry), '%P'))

ml_nome2 = tk.Label(tab2, text="Tamanho", background='#D9D9D9', font='Helvetica 9 bold')
ml_inp2 = tk.Entry(tab2, width=7, validate='key', vcmd=(root.register(validate_entry), '%P'))

pven_nome2 = tk.Label(tab2, text="Preço da venda", background='#D9D9D9', font='Helvetica 9 bold')
pven_inp2 = tk.Entry(tab2, width=7, validate='key', vcmd=(root.register(validate_entry), '%P'))

#2
tabela2 = ttk.Treeview(tab2, columns=("1", "2", "3", "4", "5", "6"), show="headings")

#2
tabela2.column("1", minwidth=0, width=50)
tabela2.heading("1", text="Qtd")
tabela2.column("2", minwidth=0, width=200)
tabela2.heading("2", text="Nome")
tabela2.column("3", minwidth=0, width=50)
tabela2.heading("3", text="mL")
tabela2.column("4", minwidth=0, width=100)
tabela2.heading("4", text="Custo total (R$)")
tabela2.column("5", minwidth=0, width=150)
tabela2.heading("5", text="Preço de venda")
tabela2.column("6", minwidth=0, width=150)
tabela2.heading("6", text="Porcentagem de lucro")

#2
qtd_nom2.grid(column=0, row=0, sticky="w")
qtd_inp2.grid(column=0, row=1, sticky="w", padx=10)
nom_nom2.grid(column=1, row=0, sticky="w")
nom_inp2.grid(column=1, row=1)
cst_nome2.grid(column=2, row=0, sticky="w")
cst_inp2.grid(column=2, row=1)
dol_nome2.grid(column=3, row=0, sticky="w")
dol_inp2.grid(column=3, row=1)
ml_nome2.grid(column=4, row=0, sticky="w")
ml_inp2.grid(column=4, row=1)
pven_nome2.grid(column=5, row=0, sticky="w")
pven_inp2.grid(column=5, row=1)

tabela2.grid(column=0, row=3, columnspan=6, pady=5, padx=10)


def dolar(tab_inp):
    val_dolar = float(tab_inp['dol_inp'].get())
    val_prod = float(tab_inp['cst_inp'].get())
    calculo = val_dolar * val_prod
    return calculo

def porcentagem_de_lucro(pven_inp2, tab_inp):
    custo = dolar(tab_inp)
    porcentagem_value = float(pven_inp2.get())
    lucro = porcentagem_value - custo
    if custo > 0:
        lucro_porcentagem = (lucro / custo) * 100
    else:
        lucro_porcentagem = 0
    return lucro_porcentagem

def porcentagens(tab_inp):
    valor = dolar(tab_inp)
    calculo = {
        "25": valor * 1.25,
        "50": valor * 1.50,
        "100": valor * 2.00,
        "200": valor * 3.00,
        "230": valor * 3.25
    }
    return calculo

def adicionar1(tab_inp, tab_table):
    if tab_inp['qtd_inp'].get() == "" or tab_inp['nom_inp'].get() == "" or tab_inp['cst_inp'].get() == "":
        messagebox.showinfo(title="Erro", message="Digite todos os dados")
        return
    resultados = porcentagens(tab_inp)
    custo_reais = dolar(tab_inp) * float(tab_inp['qtd_inp'].get())
    tab_table.insert("", "end", values=(
        tab_inp['qtd_inp'].get(), 
        tab_inp['nom_inp'].get(), 
        tab_inp['ml_inp'].get(),
        "R${:,.2f}".format(custo_reais), 
        "R${:,.2f}".format(resultados["25"]),
        "R${:,.2f}".format(resultados["50"]),
        "R${:,.2f}".format(resultados["100"]),
        "R${:,.2f}".format(resultados["200"]),
        "R${:,.2f}".format(resultados["230"]),
    ))
    tab_inp['qtd_inp'].delete(0, tk.END)
    tab_inp['nom_inp'].delete(0, tk.END)
    tab_inp['cst_inp'].delete(0, tk.END)
    tab_inp['ml_inp'].delete(0, tk.END)

def adicionar2(tab_inp, tab_table):
    if tab_inp['qtd_inp'].get() == "" or tab_inp['nom_inp'].get() == "" or tab_inp['cst_inp'].get() == "":
        messagebox.showinfo(title="Erro", message="Digite todos os dados")
        return
    
    porc_lucro = porcentagem_de_lucro(pven_inp2, tab_inp)
    custo_reais = dolar(tab_inp) * float(tab_inp['qtd_inp'].get())
    tab_table.insert("", "end", values=(
        tab_inp['qtd_inp'].get(), 
        tab_inp['nom_inp'].get(), 
        tab_inp['ml_inp'].get(),
        "R${:,.2f}".format(custo_reais),
        "R${:,.2f}".format(float(tab_inp['pven_inp2'].get())), 
        "{:,.2f}%".format(porc_lucro)
    ))
    tab_inp['qtd_inp'].delete(0, tk.END)
    tab_inp['nom_inp'].delete(0, tk.END)
    tab_inp['cst_inp'].delete(0, tk.END)
    tab_inp['ml_inp'].delete(0, tk.END)
    tab_inp['pven_inp2'].delete(0, tk.END)


def limpar(tab_table):
    try:
        itemselecionado = tab_table.selection()[0]
        tab_table.delete(itemselecionado)
    except:
        messagebox.showerror(title="Erro", message="Selecione o item para deletar")
    
def exportar1(tab_table, dol_inp, file_name):
    data = []
    for row in tab_table.get_children():
        row_data = tab_table.item(row)['values']
        row_data = list(row_data) + [dol_inp.get(), date.datetime.now()]
        data.append(row_data)
    columns = ["Quantidade", "Nome", "Tamanho (mL)", "Custo total (R$)", "25%", "50%", "100%", "200%", "230%", "Dolar", "Data"]
    df = pd.DataFrame(data, columns=columns) 
    
    try:
        df.to_excel(file_name, index=False)
        messagebox.showinfo(title="Sucesso", message="Valores exportados com sucesso!")
    except:
        messagebox.showerror(title="Erro", message="Erro ao exportar")

def exportar2(tab_table, dol_inp, file_name):
    data = []
    for row in tab_table.get_children():
        row_data = tab_table.item(row)['values']
        row_data = list(row_data) + [dol_inp.get(), date.datetime.now()]
        data.append(row_data)
    columns = ["Quantidade", "Nome", "Tamanho (mL)", "Custo total (R$)", "Preço de venda", "Porcentagem de lucro", "Dolar", "Data"]
    df = pd.DataFrame(data, columns=columns) 
    try:
        df.to_excel(file_name, index=False)
        messagebox.showinfo(title="Sucesso", message="Valores exportados com sucesso!")
    except:
        messagebox.showerror(title="Erro", message="Erro ao exportar")

tab1_inputs = {'qtd_inp': qtd_inp, 'nom_inp': nom_inp, 'cst_inp': cst_inp, 'dol_inp': dol_inp, 'ml_inp': ml_inp}
tab2_inputs = {'qtd_inp': qtd_inp2, 'nom_inp': nom_inp2, 'cst_inp': cst_inp2, 'dol_inp': dol_inp2, 'ml_inp': ml_inp2, 'pven_inp2': pven_inp2}

#1
adicionar_botao = tk.Button(tab1, text="Adicionar", command=lambda: adicionar1(tab1_inputs, tabela))
limpar_botao = tk.Button(tab1, text="Limpar", command=lambda: limpar(tabela))
exportar_botao = tk.Button(tab1, text="Exportar", command=lambda: exportar1(tabela, dol_inp, "tabela_preco.xlsx"))
#2
adicionar_botao2 = tk.Button(tab2, text="Adicionar", command=lambda: adicionar2(tab2_inputs, tabela2))
limpar_botao2 = tk.Button(tab2, text="Limpar", command=lambda: limpar(tabela2))
exportar_botao2 = tk.Button(tab2, text="Exportar", command=lambda: exportar2(tabela2, dol_inp2, "tabela_vendidos.xlsx"))
#1
adicionar_botao.grid(column=0, row=4)
limpar_botao.grid(column=1, row=4)
exportar_botao.grid(column=2, row=4)
#2
adicionar_botao2.grid(column=0, row=4)
limpar_botao2.grid(column=1, row=4)
exportar_botao2.grid(column=2, row=4)

root.mainloop()
