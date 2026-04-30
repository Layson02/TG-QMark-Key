<a id="english"></a>
# TG-QMark-Key

[🇧🇷 Ler em Português](#portugues)

This repository contains a hybrid toolset designed to quickly solve and test incomplete codes (keys containing a `?` character). The project offers two approaches: a fast web-based generator for manual copying and an advanced Python macro for automated insertion.

---

## 🚀 Project Versions

### 1. Standard Web Interface

A minimalist browser-based version focused on speed and ease of use for standard manual activation.

* **Stack:** Pure HTML, CSS, and JavaScript.
* **Instant Generation:** Replaces `?` with numbers from 9 to 0 instantly.
* **One-Click Copy:** Dedicated buttons to copy each variation to the clipboard with visual feedback (strikethrough and darkened text on copied keys).
* **Macro Integration:** Includes a "Copy List (Macro)" button to export the entire list directly to the clipboard, ready to feed the Python script.

### 2. Advanced Macro (`macro.py`)

A robust Python script designed to automate the typing and submission of keys in restricted interfaces.

* **Library:** Uses `pyautogui` for keyboard simulation and `keyboard` to capture global system shortcuts.
* **Anti-detection:** Implements random dynamic intervals (between 1.8s and 2.7s) between submissions to simulate human behavior and avoid predictable bot patterns.
* **Real-Time Controls (Hotkeys):**
    * `ESC`: Instantly terminates the program (Kill Switch) for safety.
* **Preparation Delay:** Includes a 5-second interval before initial execution, allowing you to safely switch to the target window.

---

## 🛠️ Quick Installation

To use the Advanced Macro (`macro.py`), you need to install the Python dependencies. 

**⚠️ How to open the terminal in the correct location:**
Before running the command, you need to open the terminal in the main project folder (where this README file is located). Choose the easiest method for you:

* **Method 1: Via VS Code (Recommended)**
  Open the project folder in VS Code. On the top menu, go to `Terminal > New Terminal` (or press the shortcut `` Ctrl + ` ``). The terminal will open in the correct folder.

* **Method 2: Via File Explorer (Windows)**
  Open the project folder. Right-click on an empty space and select **"Open in Terminal"**. (Ninja tip: you can also click on the folder's address bar, type `cmd` and press Enter).

* **Method 3: Manual Navigation**
  Open your system's terminal and use the `cd` command followed by the full path of where you saved the folder. 
  Example: `cd C:\Users\YourUser\Downloads\TG-QMark-Key`

With the terminal open in the right place, run the command below to install the libraries. It will automatically find the file inside the macro folder:

```bash
pip install -r macro/requirements.txt
```

[🇺🇸 Read in English](#english)

<a id="portugues"></a>

Este repositório contém um conjunto de ferramentas híbrido projetado para resolver e testar rapidamente códigos incompletos (chaves contendo um caractere `?`). O projeto oferece duas abordagens: um gerador rápido baseado em web para cópia manual e um macro avançado em Python para inserção automatizada.

---

## 🚀 Versões do Projeto

### 1. Interface Web Padrão

Uma versão minimalista baseada no navegador, focada em velocidade e facilidade de uso para ativação manual padrão.

* **Stack:** HTML, CSS e JavaScript puros.
* **Geração Instantânea:** Substitui o `?` por números de 9 até 0 instantaneamente.
* **Cópia em Um Clique:** Botões dedicados para copiar cada variação para a área de transferência com feedback visual (texto riscado e escurecido nas chaves já copiadas).
* **Integração com o Macro:** Inclui um botão "Copiar Lista (Macro)" para exportar a lista completa diretamente para a área de transferência, pronta para alimentar o script em Python.

### 2. Macro Avançado (`macro.py`)

Um script Python robusto projetado para automatizar a digitação e o envio de chaves em interfaces restritas.

* **Biblioteca:** Usa `pyautogui` para simulação de teclado e `keyboard` para capturar atalhos globais do sistema.
* **Anti-detecção:** Implementa intervalos dinâmicos aleatórios (entre 1.8s e 2.7s) entre os envios para simular o comportamento humano e evitar padrões previsíveis de bots.
* **Controles em Tempo Real (Hotkeys):**
    * `ESC`: Encerra o programa imediatamente (Kill Switch) para segurança.
* **Atraso de Preparação:** Inclui um intervalo de 5 segundos antes da execução inicial, permitindo que você mude para a janela alvo com segurança.

---

## 🛠️ Instalação Rápida

Para utilizar o Macro Avançado (`macro.py`), é necessário instalar as dependências do Python. 

**⚠️ Como abrir o terminal no local correto:**
Antes de rodar o comando, você precisa abrir o terminal na pasta principal do projeto (onde está este arquivo README). Escolha o método mais fácil para você:

* **Método 1: Pelo VS Code (Recomendado)**
  Abra a pasta do projeto no VS Code. No menu superior, vá em `Terminal > Novo Terminal` (ou pressione o atalho `` Ctrl + ` ``). O terminal já abrirá na pasta correta.

* **Método 2: Pelo Explorador de Arquivos (Windows)**
  Abra a pasta do projeto. Clique com o botão direito em um espaço vazio e selecione **"Abrir no Terminal"**. (Dica ninja: você também pode clicar na barra de endereços da pasta, digitar `cmd` e apertar Enter).

* **Método 3: Navegação Manual**
  Abra o terminal do seu sistema e use o comando `cd` seguido do caminho completo de onde você salvou a pasta. 
  Exemplo: `cd C:\Users\SeuUsuario\Downloads\TG-QMark-Key`

Com o terminal aberto no local certo, execute o comando abaixo para instalar as bibliotecas. Ele já vai buscar o arquivo automaticamente dentro da pasta do macro:

```bash
pip install -r macro/requirements.txt
