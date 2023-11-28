import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")

# Aggiungere tutti i file modificati
run_command("git add .")

# Fare il commit con un messaggio
run_command('git commit -m "update"')

# Fare il push dei cambiamenti
run_command("git push")
