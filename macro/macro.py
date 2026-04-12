import pyautogui
import time
import random
import keyboard
import sys

def iniciar_macro():
    print("Cole a lista de chaves geradas pelo site (pressione Enter duas vezes para iniciar):")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha.strip())

    if not linhas:
        print("\n[X] Nenhuma chave fornecida. Encerrando.")
        sys.exit()

    print("\n[!] ATENÇÃO: Você tem 5 segundos para focar no campo de código da Steam.")
    print("[!] Pressione 'ESC' a qualquer momento para abortar o script.\n")
    time.sleep(5)

    for chave in linhas:
        if keyboard.is_pressed('esc'):
            print("\n[!] Processo cancelado pelo usuário.")
            sys.exit()

        try:
            pyautogui.typewrite(chave, interval=0.01)
            pyautogui.press('enter')
            print(f"-> Chave inserida: {chave}")
            
            delay = random.uniform(1.8, 2.7)
            time.sleep(delay)
            
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')

        except Exception as e:
            print(f"\n[X] Erro inesperado durante a execução: {e}")
            sys.exit()

    print("\n[+] Todas as chaves foram processadas.")

if __name__ == "__main__":
    iniciar_macro()