import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import os

def seleccionar_directorio():
    global directorio_destino
    directorio_destino = filedialog.askdirectory()
    if directorio_destino:
        etiqueta_directorio.config(text=f"Directorio: {directorio_destino}")
    else:
        etiqueta_directorio.config(text="No se ha seleccionado ningún directorio")

def descargar_video():
    url = entrada_url.get()
    if not url:
        etiqueta_estado.config(text="Por favor, ingresa una URL")
        return
    if not directorio_destino:
        etiqueta_estado.config(text="Por favor, selecciona un directorio")
        return

    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(directorio_destino)
        etiqueta_estado.config(text="¡Descarga completa!")
    except Exception as e:
        etiqueta_estado.config(text=f"Error: {e}")

#Aun hay errores con la extensión
def descargar_mp3():
    url = entrada_url.get()
    if not url:
        etiqueta_estado.config(text="Por favor, ingresa una URL")
        return
    if not directorio_destino:
        etiqueta_estado.config(text="Por favor, selecciona un directorio")
        return
    try:
        yt = YouTube(url)
        mp3 = yt.streams.filter(only_audio=True).first()
        mp3.download(directorio_destino)
        etiqueta_estado.config(text="¡Descarga completa!")
    except Exception as e:
        etiqueta_estado.config(text=f"Error: {e}")


root = tk.Tk()
root.title("Descargador de Videos de Kuroky")

etiqueta_url = tk.Label(root, text="URL del video:")
etiqueta_url.pack()

entrada_url = tk.Entry(root, width=100)
entrada_url.pack()

boton_seleccionar_directorio = tk.Button(root, text="Seleccionar directorio", command=seleccionar_directorio)
boton_seleccionar_directorio.pack()

etiqueta_directorio = tk.Label(root, text="No se ha seleccionado ningún directorio")
etiqueta_directorio.pack()

boton_descargar_video = tk.Button(root, text="Descargar Video", command=descargar_video)
boton_descargar_video.pack()

boton_descargar_mp3 = tk.Button(root, text="Descargar mp3", command=descargar_mp3)
boton_descargar_mp3.pack()

etiqueta_estado = tk.Label(root, text="")
etiqueta_estado.pack()

directorio_destino = ""

root.mainloop()
