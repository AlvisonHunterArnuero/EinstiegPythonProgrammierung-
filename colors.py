colores = { "Normal":"\033[0m", "Resaltado" : "\033[1m",
 "Gris" : "\033[2m", "Cursiva" : "\033[3m",
 "Subrayado" : "\033[4m", "Parpadeo" : "\033[5m",
 "Inverso" : "\033[7m", "GrisOscuro" : "\033[8m",
 "Tachado" : "\033[9m", "DobleSub" : "\033[21m",
 "Negro" : "\033[30m" , "Rojo" : "\033[31m",
 "Verde" : "\033[32m", "Marron" : "\033[33m",
 "Azul" : "\033[34m", "Morado" : "\033[35m",
 "Celeste" : "\033[36m", "Gris" : "\033[37m",
 "Rosado" : "\033[91m", "VerdeClaro" : "\033[92m",
 "AmarilloClaro" : "\033[93m", "AzulClaro" : "\033[94m",
 "MoradoClaro" : "\033[95m", "CianClaro" : "\033[96m",
 "Blanco" : "\033[97m", "SupraRayado" : "\033[53m",
 "FRojo" : "\033[41m", "FVerde" : "\033[42m",
 "FMarron" : "\033[43m", "FAzul" : "\033[44m",
 "FMorado" : "\033[45m", "FCeleste" : "\033[46m",
 "FGris" : "\033[47m" , "FGrisClaro" : "\033[100m",
 "FRosado" : "\033[101m" , "FVerdeClaro" : "\033[102m",
 "FAmarillo" : "\033[103m" , "FAzulClaro" : "\033[104m",
 "FMoradoClaro" : "\033[105m" , "FCianClaro" : "\033[106m",
 "FBlanco" : "\033[107m" }
for i in colores:
 print (colores[i],i, "\033[0m")
