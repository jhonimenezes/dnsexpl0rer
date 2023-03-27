import requests
import signal
import os
import pyfiglet
from colorama import Fore, Style
from tqdm import tqdm


#Função para verificar se o diretório está ativo
def verificar_diretorio_ativo(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except:
        return False
    
#Função para tratar o sinal de interrupção
def interromper_execucao(signal, frame):
    print(f" \n\n {Fore.RED}[XX]  O usuário interrompeu a execução do programa.{Style.RESET_ALL}\n")
    exit(0)

#Define o tratador de sinal para o sinal SIGINT
signal.signal(signal.SIGINT, interromper_execucao)

#Cria uma arte em ASCII na parte superior
ascii_art = pyfiglet.figlet_format("ExDNS")

#Imprime a arte na tela
os.system('cls' if os.name == 'nt' else 'clear')
print(ascii_art)
print(f"{Fore.YELLOW} --------------------------- {Style.RESET_ALL}")
print(f"{Fore.YELLOW} |Desenvolvido por: Mr.Jhoni|{Style.RESET_ALL}")
print(f"{Fore.YELLOW} --------------------------- {Style.RESET_ALL}")
    

try:
    
    #Solicita o endereço do host ao usuario
    host = input("\nDigite o endereço do host: ")

    #Solicita o nome da wordlist ao usuario
    wordlist = input("Digite o nome da wordlist: ")


    #Lê os diretórios a partir da wordlist
    with open(wordlist, 'r') as f:
        diretorios = f.read().splitlines()

    #percorre a lista de diretórios comuns para tentar acessar cada um deles
    for diretorio in tqdm(diretorios):
        
        #Verifica se o sinal de interrupção foi recebido
        signal.signal(signal.SIGINT, interromper_execucao)

        url = f"http://{host}/{diretorio}"
        if verificar_diretorio_ativo(url):
            print(f"\n[+] O diretório {url} está ativo.")

#Tratamento de possíveis erros e interrupções            
except FileExistsError:
    print(f"{Fore.YELLOW} [!] {Style.RESET_ALL} O arquivo {wordlist} não foi encontrado.")
except requests.exceptions.ConnectionError:
    print(f"{Fore.RED} [X] Não foi possível conectar ao host {Style.RESET_ALL} {host}.")
except Exception as e:
    print(f"{Fore.BLUE} [E] {Style.RESET_ALL} ocorreu um erro: {e}.")