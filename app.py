import tkinter as tk
import webbrowser

janela = tk.Tk()
janela.title("Meus Atalhos")
janela.geometry("300x250")


def abrir_google():
    webbrowser.open("https://google.com")


def abrir_youtube():
    webbrowser.open("https://youtube.com")


def abrir_whatsapp():
    webbrowser.open("https://web.whatsapp.com")


titulo = tk.Label(janela, text="Meus Atalhos", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

btn_google = tk.Button(janela, text="Abrir Google", command=abrir_google, width=20, height=2)
btn_google.pack(pady=5)

btn_youtube = tk.Button(janela, text="Abrir YouTube", command=abrir_youtube, width=20, height=2)
btn_youtube.pack(pady=5)

btn_whats = tk.Button(janela, text="Abrir WhatsApp", command=abrir_whatsapp, width=20, height=2)
btn_whats.pack(pady=5)

janela.mainloop()
