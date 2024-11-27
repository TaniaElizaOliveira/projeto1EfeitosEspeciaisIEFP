import os
import sys
import re
import subprocess

def obter_mac(ipv4):
    try:
        comando = 'arp -a' if os.name == 'nt' else 'arp -n'
        resultado = subprocess.check_output(comando, shell=True, text=True)
        padrao = rf"{ipv4}\s+\w+\s+([a-fA-F0-9:.-]+)"
        match = re.search(padrao, resultado)
        if match:
            return match.group(1)
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando ARP: {e}")
        return None

def refrescar_cache(ipv4):
    try:
        comando = ['ping', '-c', '1', ipv4] if os.name != 'nt' else ['ping', '-n', '1', ipv4]
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erro ao enviar ping para {ipv4}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python l2addr.py [-r] ipv4_addr1 [ipv4_addr2 ...]")
        return

    argumentos = sys.argv[1:]
    refrescar = False

    if "-r" in argumentos:
        refrescar = True
        argumentos.remove("-r")
    
    if not argumentos:
        print("Erro: Nenhum endereço IPv4 fornecido.")
        return

    for ipv4 in argumentos:
        if refrescar:
            print(f"Refrescando cache ARP para {ipv4}...")
            refrescar_cache(ipv4)
        
        print(f"Buscando endereço MAC para {ipv4}...")
        mac = obter_mac(ipv4)

        if mac:
            print(f"IPv4: {ipv4} -> MAC: {mac}")
        else:
            print(f"IPv4: {ipv4} -> MAC: Não encontrado.")

if __name__ == "__main__":
    main()
