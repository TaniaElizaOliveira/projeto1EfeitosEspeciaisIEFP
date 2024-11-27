import os
import time
import sys


def efeito_diagonal_esquerda(texto):
    for i, char in enumerate(texto):
        print(" " * i + char)

def efeito_diagonal_direita_invertida(texto):
    texto_invertido = texto[::-1]
    for i, char in enumerate(texto_invertido):
        print(" " * (len(texto_invertido) - i - 1) + char)

def efeito_diagonais_cruzadas(texto):
    tamanho = len(texto)
    for i in range(tamanho):
        linha = [" "] * tamanho
        linha[i] = texto[i]
        linha[tamanho - i - 1] = texto[i]
        print("".join(linha))

def efeito_diagonal_palavras_inversas(texto):
    palavras = texto.split()
    for i, palavra in enumerate(reversed(palavras)):
        print(" " * i + palavra)

def efeito_em_v(texto):
    tamanho = len(texto)
    for i in range((tamanho + 1) // 2):
        espacos_iniciais = " " * i
        espacos_centro = " " * (tamanho - 2 * i - 2)
        if i == (tamanho - 1) // 2:
            print(espacos_iniciais + texto[i])
        else:
            print(espacos_iniciais + texto[i] + espacos_centro + texto[tamanho - i - 1])

def efeito_texto_deslizante(texto, intervalo=0.5):
    largura_linha = 40
    texto_com_espacos = texto + " " * (largura_linha - len(texto))
    texto_circular = texto_com_espacos * 2

    try:
        while True:
            for i in range(len(texto_com_espacos)):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(texto_circular[i:i + largura_linha])
                time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nEfeito interrompido pelo usuário.")


def exibir_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
****************************************************
*                                                  *
*  EFEITO                                          *
*                                                  *
*    1 - Diagonal Esquerda                         *
*    2 - Diagonal Direita, Texto Invertido         *
*    3 - Diagonais Cruzadas                        *
*    4 - Diagonal Direita, Palavras Ordem Inversa  *
*    5 - Em V                                      *
*    6 - Deslizante                                *
*    T - Todos                                     *
*    E - Encerrar                                  *
*                                                  *
****************************************************
    """)


def main():
    if len(sys.argv) < 2:
        print("Uso: python efeitos.py [-i intervalo] palavra1 [palavra2] ... [palavraN]")
        return

    intervalo = 0.5 
    argumentos = sys.argv[1:]

   
    if "-i" in argumentos:
        index = argumentos.index("-i")
        try:
            intervalo = float(argumentos[index + 1])
            argumentos = argumentos[:index] + argumentos[index + 2:]
        except (IndexError, ValueError):
            print("Erro: valor inválido para o intervalo. Usando valor padrão de 0.5s.")

    texto = " ".join(argumentos)

    while True:
        exibir_menu()
        opcao = input("OPÇÃO> ").strip().upper()

        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_diagonal_esquerda(texto)
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_diagonal_direita_invertida(texto)
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_diagonais_cruzadas(texto)
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_diagonal_palavras_inversas(texto)
            input("\nPressione ENTER para continuar...")

        elif opcao == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_em_v(texto)
            input("\nPressione ENTER para continuar...")

        elif opcao == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_texto_deslizante(texto, intervalo)

        elif opcao == "T":
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_diagonal_esquerda(texto)
            input("\nPressione ENTER para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_diagonal_direita_invertida(texto)
            input("\nPressione ENTER para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_diagonais_cruzadas(texto)
            input("\nPressione ENTER para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_diagonal_palavras_inversas(texto)
            input("\nPressione ENTER para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_em_v(texto)
            input("\nPressione ENTER para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            efeito_texto_deslizante(texto, intervalo)

        elif opcao == "E":
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)

if __name__ == "__main__":
    main()
