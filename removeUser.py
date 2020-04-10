def RemoveUser(arg):
    valv = arg
    if valv == True:
        lstMoledores = ["Morenito", "Chinito", "Billicito", "Elotito"]
        name = lstMoledores[0]
        lstMoledores.remove(name)
        print("el usuario " +name+ " fue mandado al diablo!")
        return
RemoveUser(True)
