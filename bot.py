import pyautogui
import time

mensaje = (input("Cual es el mensaje?: "))
repeticiones = int(input("Cuantos mensajes quieres enviar?: "))
time.sleep(5)
for _ in range(repeticiones):
    pyautogui.write(mensaje, interval=0.000001)
    pyautogui.press('enter')
    time.sleep(1)
