from tkinter import *

root=Tk()	
menu=Menu(root)
root.config(menu=menu)
#root.minsize(width=1360, height=720)
root.wm_title("Inspérmon")

#     ===================  Toolbar  ==================
arquivo=Menu(menu)
menu.add_cascade(label="Arquivo", menu=arquivo)
arquivo.add_command(label="Salvar")#, command=)
arquivo.add_command(label="Abrir")#, command=)

ajuda=Menu(menu)
menu.add_command(label="Ajuda")#, command=open.ajuda)

#    ======================= Interface Inicial =======================
#botão do iniciais
pokemon_inicial = Label(root, text="Escolha seu Ispérmon inicial")
pokemon_inicial.grid(row=0, columnspan=3)
sharmander = Button(root, text="Sharmander")#, command=)
sharmander.grid(row=3)
bulbatauro = Button(root, text="Bulbatauro")#, command=)
bulbatauro.grid(row=3,column=1)
skuirtle = Button(root, text="Skuirtle")#, command=)
skuirtle.grid(row=3,column=2)

# fotos dos iniciais
fotosharmander = PhotoImage(file="Sharmander.png")
sharmanderlabel = Label(root, image=fotosharmander)
sharmanderlabel.grid(row=1, ipadx=50)
	
fotobulbatauro = PhotoImage(file="Bulbatauro.png")
bulbataurolabel = Label(root, image=fotobulbatauro)
bulbataurolabel.grid(row=1,column=1, ipadx=50)

fotoskuirtle = PhotoImage(file="Skuirtle.png")
skuirtlelabel = Label(root, image=fotoskuirtle)
skuirtlelabel.grid(row=1,column=2, ipadx=50)


root.mainloop()
