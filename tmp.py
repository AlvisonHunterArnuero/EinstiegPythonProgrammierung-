def get_help(helpMate):
    if (helpMate.upper().find('HOSMEL') != -1):
        print('Buscalo en Google!!')
    elif(helpMate=='' or helpMate==' '):
        print('No ingresastes ningun nombre')
    else:
        print("En que puedo ayudarte?")

get_help('Hosmelcito')
