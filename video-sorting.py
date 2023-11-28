import os
import re

def extract_number(name):
    # Estrae il numero dal nome della cartella usando una espressione regolare
    match = re.search(r'\d+', name)
    return int(match.group()) if match else 0

def create_directories_from_file(file_path, main_folder):
    directories = []

    # Assicurarsi che la cartella principale esista
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)

    try:
        with open(file_path, 'r') as file:
            for line in file:
                directory_name = line.strip()
                full_path = os.path.join(main_folder, directory_name)
                
                if directory_name and not os.path.exists(full_path):
                    os.makedirs(full_path)
                    print(f"Cartella '{full_path}' creata.")
                    directories.append(directory_name)
                else:
                    print(f"Cartella '{full_path}' già esiste o non è un nome valido.")
        
        # Ordinamento decrescente basato sui numeri nel nome
        directories.sort(key=extract_number, reverse=True)
        return directories

    except FileNotFoundError:
        print(f"Il file {file_path} non è stato trovato.")
        return []
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        return []

# Percorso del file account.txt e della cartella principale
file_path = 'accounts.txt'
main_folder = 'Account-Sorted'

# Creazione delle cartelle e stampa dell'array ordinato
sorted_directories = create_directories_from_file(file_path, main_folder)
print("Cartelle ordinate:", sorted_directories)
