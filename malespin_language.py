# Esta es una antigua Forma de comunicacion inventada por un famoso general salvadoreño
# llamado Francisco Malespin en 1845 a las tropas en el salvador, honduras y nicaragua.
# Made with ❤️ in Python 3 by Alvison Hunter - November 27th, 2020
IN = "aeiobtmpfgcsAEIOBTMPFGCSéáíóúÉÁÍÓÚ"
OUT = "eaoitbpmgfscEAOITBPMGFSCáéóíúÁÉÓÍÚ"


def encrypt_phrase():
    str = input('Enter the Phrase you want to be Encrypted: \n')
    print("\n==============================================================")
    print('Please find below your encrypted phrase:')
    print("==============================================================")
    print(str.translate(str.maketrans(IN, OUT)))


encrypt_phrase()
