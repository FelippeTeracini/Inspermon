from tkinter import *

root=Tk()	

menu=Menu(root)
root.config(menu=menu)
root.wm_title("Inspérmon")
#root.wm_pack(side=LEFT)

arquivo=Menu(menu)
menu.add_cascade(label="Arquivo", menu=arquivo)
arquivo.add_command(label="Salvar")#, command=)
arquivo.add_command(label="Abrir")#, command=)

ajuda=Menu(menu)
menu.add_command(label="Ajuda")#, command=open.ajuda)

root.mainloop()


