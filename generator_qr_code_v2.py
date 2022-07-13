import tkinter as tk
import qrcode
import pathlib
import datetime

window= tk.Tk()
window.title('Générateur de QR Code')

canvas = tk.Canvas(window, width = 400, height = 300)
canvas.pack()

QRCode = canvas.create_text(200, 50, text="Générateur de QR Code", font="Arial 16 bold", fill="black")

inputLink = tk.Entry (window) 
canvas.create_window(200, 120, window=inputLink)

def generatorQrCode():
    link = inputLink.get()
    if link:
        labelLink = tk.Label(window, text= link)
        canvas.create_window(200, 230, window=labelLink)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(link)
        qr.make(fit=True)

        now = datetime.datetime.now()
        name = now.strftime("%Y-%m-%d-%H-%M-%S")

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(str(name)+".png")

        path = pathlib.Path().resolve()

        noError = tk.Label(window, text="Information sur le QR Code généré \n\n Nom du QR Code : " + str(name) + " .png \n Contenu suivant : " + link + " \n Dossier : " + str(path))
        canvas.create_window(200, 230, window=noError)
    else :
        error = tk.Label(window, text="Merci de renseigner le champ ci-dessus pour générer un QR Code")
        canvas.create_window(200, 230, window=error)
    
button = tk.Button(text='Générer le QR Code', command=generatorQrCode)
canvas.create_window(200, 160, window=button)

window.mainloop()
