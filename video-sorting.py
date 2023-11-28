import os

def create_directories_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                directory_name = line.strip()
                if directory_name and not os.path.exists(directory_name):
                    os.makedirs(directory_name)
                    print(f"Cartella '{directory_name}' creata.")
                else:
                    print(f"Cartella '{directory_name}' già esiste o non è un nome valido.")
    except FileNotFoundError:
        print(f"Il file {file_path} non è stato trovato.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# Percorso del file account.txt
file_path = 'accounts.txt'

# Creazione delle cartelle
create_directories_from_file(file_path)
