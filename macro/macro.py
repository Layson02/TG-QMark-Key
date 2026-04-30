import pyautogui
import time
import random
import keyboard
import sys

def iniciar_macro():
    # 1. Coleta das chaves
    print("Cole a lista de chaves geradas pelo site (pressione Enter DUAS vezes para finalizar a lista):")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha.strip())

    if not linhas:
        print("\n[X] Nenhuma chave fornecida. Encerrando.")
        sys.exit()

    # 2. Configuração do Intervalo
    print("\n" + "="*30)
    print(" CONFIGURAÇÃO DE INTERVALO")
    print("="*30)
    print("O padrão insere um atraso entre 1.8s e 2.7s após cada tentativa.")
    intervalo_input = input("Digite o intervalo base em segundos (ou apenas pressione ENTER para o padrão): ")
    
    if intervalo_input.strip() == "":
        min_delay, max_delay = 1.8, 2.7
        print("-> Usando intervalo padrão (1.8s - 2.7s).")
    else:
        try:
            base_delay = float(intervalo_input.replace(',', '.'))
            min_delay = max(0.1, base_delay - 0.2)
            max_delay = base_delay + 0.2
            print(f"-> Usando intervalo personalizado (aprox. {base_delay}s com leve variação aleatória).")
        except ValueError:
            print("-> Valor inválido. Usando o intervalo padrão (1.8s - 2.7s).")
            min_delay, max_delay = 1.8, 2.7

    # 3. Aviso e Contagem Regressiva
    print("\n" + "="*30)
    print(" PREPARAÇÃO PARA INÍCIO")
    print("="*30)
    print("[!] Após iniciar, você terá exatamente 5 SEGUNDOS para focar a janela alvo.")
    input("Pressione ENTER quando estiver pronto para iniciar a contagem regressiva...")

    print("\n[!] Contagem iniciada! Mude para a janela alvo e clique no campo de texto AGORA.")
    for i in range(5, 0, -1):
        print(f"  Iniciando em {i}...")
        time.sleep(1)

    print("\n[!] Executando macro... Pressione 'ESC' a qualquer momento para abortar.\n")

    # 4. Execução do Macro
    for chave in linhas:
        if keyboard.is_pressed('esc'):
            print("\n[!] Processo cancelado imediatamente pelo usuário.")
            sys.exit()

        try:
            # Digita a chave
            pyautogui.typewrite(chave, interval=0.01)
            # Confirma
            pyautogui.press('enter')
            print(f"-> Chave inserida: {chave}")
            
            # Aguarda o intervalo definido
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)
            
            # Limpa o campo para a próxima tentativa
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')

        except Exception as e:
            print(f"\n[X] Erro inesperado durante a execução: {e}")
            sys.exit()

    print("\n[+] Todas as chaves foram processadas.")

if __name__ == "__main__":
    iniciar_macro()