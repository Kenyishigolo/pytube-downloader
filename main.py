import tkinter as tk
from pytube import YouTube


def descargar_video():
    url = entrada_url.get()
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    etiqueta_estado.config(text="¡Descarga completa!")

root = tk.Tk()
root.title("Descargador de Videos version Kuroky xD")

etiqueta_url = tk.Label(root, text="URL del video:")
etiqueta_url.pack()

entrada_url = tk.Entry(root, width=60)
entrada_url.pack()

boton_descargar = tk.Button(root, text="Descargar", command=descargar_video)
boton_descargar.pack()

etiqueta_estado = tk.Label(root, text="")
etiqueta_estado.pack()

root.mainloop()
