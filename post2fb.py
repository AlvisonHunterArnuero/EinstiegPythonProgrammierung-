import pyautogui
import time
message = '''
Add your message here.
'''
link = 'https://www.jcchouinard.com/'
groups=["177151769719998","275366519230814","2630047207281086","coperar","ProgramadoresEnPython3","912523932450311","CienciaDeDatosPy","JavAndroidMexico","pythonco","mi.grupo.python","nodejslatinoamerica","pythonmx","python593","pythoncr","programa.python","programadorees","stacknews","programadoressv","MundoProgramadores","191195149178008","ProgramadoresEnPython","292999948477617","Python-Latinoamérica-1401923520023037","python","PythonDevelopers","pythonicaragua","python.devz","539992333052727","142201439713193","251560641854558"]

time.sleep(5)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    print("Waiting for 45 seconds\n")
    time.sleep(45)

    pyautogui.typewrite('p')
    time.sleep(2)
    print("Writing post\n")
    pyautogui.typewrite("Hello there, it's a testing post from messy programmers")
    time.sleep(4)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

    time.sleep(3)

    pyautogui.write(['f6'])
    time.sleep(1)
