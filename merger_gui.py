from modulos.docMerger import *
import customtkinter, tkinter.messagebox

def caller():
    merger = docManager()
    merger.merger(entry_path.get())
    tkinter.messagebox.showinfo("Concluído", "Documento criado")

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry("500x300")
root.title("Word Merger")

entry_path = customtkinter.CTkEntry(master=root, placeholder_text="Digite o caminho dos arquivos")
entry_path.pack()

button = customtkinter.CTkButton(master=root, text="Juntar", command=caller)
button.pack()

root.mainloop()