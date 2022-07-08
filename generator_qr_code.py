from turtle import fillcolor
import qrcode

def generatorQrCode(link, name) :
    # on definit la taille du qr code et la gestion de visibilité
    qr = qrcode.QRCode(
        # de 1 à 40 - la taille 1 correspond à une dimension de 21x21
        version=1,
        # ERROR_CORRECT_L = 7% ou moins
        # ERROR_CORRECT_M (default) = 15% ou moins 
        # ERROR_CORRECT_Q = 25% ou moins
        # ERROR_CORRECT_H = 30% ou moins
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    # mettre le lien dans le qr code
    qr.add_data(link)
    # compile la var link en un array qr code
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(name+".png")


generatorQrCode(
    link = input("Entrez le text ou l'url que vous souhaitez retourner via le QR Code :"),
    name = input("Nomez l'image du QR Code qui sera généré : ")
)
