import subprocess
import re
from pathlib import Path
import sys
import shutil

# --- 1. Configuração ---
NETWORKS = [
    "rede-ISP",
    "proxy",
    "rede-Client1",
    "rede-Client2",
    "rede-Client3",
]

ZONEFILE_PATH = Path("./ISP/DNS")
IP_PLACEHOLDER = "IP_PLACEHOLDER"

DOCKER_COMPOSE = [
    {"name": "Cliente-1", "path": "Clientes/Cliente-1/docker-compose.yaml"},
    {"name": "Cliente-2", "path": "Clientes/Cliente-2/docker-compose.yaml"},
    {"name": "Cliente-3", "path": "Clientes/Cliente-3/docker-compose.yaml"},
    {"name": "ISP",       "path": "ISP/docker-compose.yaml"               },
]

def run_command(command):
    print(f"\n$ {' '.join(command)}")
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro: O comando falhou com o código de saída {e.returncode}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)


def create_docker_networks():
    print("==> Criando redes Docker...")
    for name in NETWORKS:
        check_command = ["docker", "network", "inspect", name]
        return_code = subprocess.run(check_command, capture_output=True).returncode

        if return_code == 0:
            print(f"  - A rede '{name}' já existe. Prosseguindo.")
        else:
            print(f"  - Criando rede: {name}")
            create_command = ["docker", "network", "create", name]
            run_command(create_command)

    print("Todas as redes foram criadas com sucesso.")


def get_host_ip_from_user():
    print("==> Por favor, digite o endereço IP da sua máquina local.")
    host_ip = input("Seu IP: ")

    if not host_ip:
        print("Erro: Nenhum endereço IP foi digitado. Saindo.")
        sys.exit(1)
        
    print(f"IP do Host digitado: {host_ip}")
    return host_ip


def update_bind9_zone_files(host_ip):
    print(f"==> Criando e atualizando arquivos de zona BIND9 a partir de modelos com o IP: {host_ip}")

    if not ZONEFILE_PATH.is_dir():
        print(f"Erro: Diretório de arquivo de zona BIND9 não encontrado: {ZONEFILE_PATH}")
        sys.exit(1)

    for template_file in ZONEFILE_PATH.glob("*.bkp"):
        target_file = template_file.with_suffix('') # Remove o sufixo .bkp
        
        print(f"  - Criando arquivo: {target_file.name}")
        
        # Copia o arquivo de modelo para o novo nome de arquivo
        shutil.copyfile(template_file, target_file)
        
        # Lê o conteúdo do arquivo recém-criado
        with open(target_file, "r") as f:
            content = f.read()

        # Substitui o espaço reservado
        new_content = re.sub(IP_PLACEHOLDER, host_ip, content)

        # Escreve o novo conteúdo de volta no arquivo
        with open(target_file, "w") as f:
            f.write(new_content)

    print("Todos os arquivos de zona BIND9 criados e atualizados com sucesso.")


def run_docker_composes():
    print("==> Iniciando projetos Docker Compose...")
    for project in DOCKER_COMPOSE:
        project_name = project["name"]
        compose_file_path = project["path"]
        
        print(f"  - Iniciando projeto: {project_name} em {compose_file_path}...")
        
        command = ["docker-compose", "-f", compose_file_path, "up", "-d"]
        run_command(command)
        
    print("Todos os serviços Docker Compose estão em execução!")


def main():
    print("=========================================")
    print("== Script de Configuração de Projeto Docker (Python) ==")
    print("=========================================")
    
    create_docker_networks()
    
    host_ip = get_host_ip_from_user()
    
    update_bind9_zone_files(host_ip)
    
    run_docker_composes()
    
    print("\n=========================================")
    print("  Configuração concluída com sucesso!         ")
    print("=========================================")


if __name__ == "__main__":
    main()
