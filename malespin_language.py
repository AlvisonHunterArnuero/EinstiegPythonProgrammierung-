# Esta es una antigua Forma de comunicacion inventada por un famoso general salvadoreño
# llamado Francisco Malespin en 1845 a las tropas en el salvador, honduras y nicaragua.
# Made with ❤️ in Python 3 by Alvison Hunter - November 27th, 2020
IN = "aeiobtmpfgcsAEIOBTMPFGCSéáíóúÉÁÍÓÚ"
OUT = "eaoitbpmgfscEAOITBPMGFSCáéóíúÁÉÓÍÚ"
#Frenede ac le souded pec elafra de Noserefue
#Granada es la ciudad más alegre de Nicaragua
def encrypt_phrase():
    name = input('Hi, Please Enter Your Name: \n')
    str = input(f'{name}, Enter the Phrase you want to be Encrypted: \n')
    print("\n============================================")
    print(f'All set {name}! Here is your encrypted phrase:')
    print("============================================")
    print (str.translate(str.maketrans(IN, OUT)))

encrypt_phrase()
