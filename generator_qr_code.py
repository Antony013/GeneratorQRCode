from argparse import ArgumentParser
import qrcode
import pathlib

# description du script
parser = ArgumentParser(
    prog='Générateur de QR Code.',
    description='Génère un QR code avec comme contenu l\'information renseigné.\nLe QR Code sera généré sous le nom donnée en argument -n sous le formati .png.\nRenseignez le nom du QR Code sans indiquer le format.'
)

# ajouter des arguments au script
parser.add_argument("-c", "--content", help="Contenu du QR Code", type=str)
parser.add_argument("-n", "--name", help="Nom du QR Code", type=str)

# on recup la commande
args = parser.parse_args()


def generatorQrCode(link, name):
    # on definit la taille du qr code et la gestion de visibilité
    qr = qrcode.QRCode(
        # de 1 à 40 - la taille 1 correspond à une dimension de 21x21
        version=1,
        # definit le pourcentage de correction quand c'est moins visible
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


if args.content is not None and args.name is not None:
    try:
        generatorQrCode(link=args.content, name=args.name)
    except:
        print("Erreur dans l'un des arguments données.")
    else:
        print("\nLe QR Code a bien été généré au nom de : " + str(args.name) +
              ".png à l'adresse : " + str(pathlib.Path().resolve()) + "\n")
else:
    print("Arguments nécessaires incorrects. -h pour de l'aide.")
