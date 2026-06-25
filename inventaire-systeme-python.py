import psutil
import socket
import platform
import csv
from datetime import datetime

def get_infos_systeme():
    """Collecte les informations principales du système."""

    # Nom de la machine et IP
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Non disponible"

    # Système d'exploitation
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()

    # RAM
    ram = psutil.virtual_memory()
    ram_total_go = round(ram.total / (1024 ** 3), 2)
    ram_utilisee_go = round(ram.used / (1024 ** 3), 2)
    ram_pourcentage = ram.percent

    # Disque (partition principale)
    disque = psutil.disk_usage('/')
    disque_total_go = round(disque.total / (1024 ** 3), 2)
    disque_utilise_go = round(disque.used / (1024 ** 3), 2)
    disque_pourcentage = disque.percent

    # CPU
    cpu_physiques = psutil.cpu_count(logical=False)
    cpu_logiques = psutil.cpu_count(logical=True)
    cpu_utilisation = psutil.cpu_percent(interval=1)

    # Date de collecte
    date_collecte = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "Date de collecte": date_collecte,
        "Hostname": hostname,
        "Adresse IP": ip,
        "OS": f"{os_name} {os_release}",
        "Version OS": os_version,
        "RAM totale (Go)": ram_total_go,
        "RAM utilisée (Go)": ram_utilisee_go,
        "RAM utilisée (%)": ram_pourcentage,
        "Disque total (Go)": disque_total_go,
        "Disque utilisé (Go)": disque_utilise_go,
        "Disque utilisé (%)": disque_pourcentage,
        "CPU physiques": cpu_physiques,
        "CPU logiques": cpu_logiques,
        "CPU utilisation (%)": cpu_utilisation,
    }

def afficher_infos(infos):
    """Affiche les informations dans le terminal."""
    print("\n" + "="*50)
    print("       INVENTAIRE SYSTÈME")
    print("="*50)
    for cle, valeur in infos.items():
        print(f"  {cle:<25} : {valeur}")
    print("="*50 + "\n")

def exporter_csv(infos, nom_fichier="inventaire.csv"):
    """Exporte les informations dans un fichier CSV."""
    with open(nom_fichier, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=infos.keys())
        writer.writeheader()
        writer.writerow(infos)
    print(f"Export CSV généré : {nom_fichier}")

if __name__ == "__main__":
    infos = get_infos_systeme()
    afficher_infos(infos)
    exporter_csv(infos)