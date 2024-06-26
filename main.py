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

def descargar_audio():
    url = entrada_url.get()
    if not url:
        etiqueta_estado.config(text="Por favor, ingresa una URL")
        return
    if not directorio_destino:
        etiqueta_estado.config(text="Por favor, selecciona un directorio")
        return

    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        descarga_audio = audio.download(directorio_destino)
        base, _ = os.path.splitext(descarga_audio)  # Ignoramos la extensión en esta variable
        nuevo_archivo = base + '.mp3'
        os.rename(descarga_audio, nuevo_archivo)
        etiqueta_estado.config(text="¡Descarga de audio completa!")
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

boton_descargar = tk.Button(root, text="Descargar Video", command=descargar_video)
boton_descargar.pack()

boton_descargar_audio = tk.Button(root, text="Descargar Audio", command=descargar_audio)
boton_descargar_audio.pack()

etiqueta_estado = tk.Label(root, text="")
etiqueta_estado.pack()

directorio_destino = ""

root.mainloop()
