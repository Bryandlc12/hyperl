import os
import subprocess
from datetime import datetime, timedelta

# Configuración
num_commits = 20  # Número de commits a generar
dias_atras = 120  # Días hacia atrás desde la fecha actual

# Iterar y hacer commits en fechas anteriores
for i in range(num_commits):
    fecha_commit = (datetime.now() - timedelta(days=dias_atras - i)).strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear un archivo para cada commit
    file_name = f"archivo_{i+1}.txt"
    with open(file_name, "w") as f:
        f.write(f"Commit {i+1} realizado el {fecha_commit}\n")

    # Ejecutar comandos Git
    os.system(f"git add {file_name}")
    commit_cmd = f'GIT_COMMITTER_DATE="{fecha_commit}" git commit -m "Commit {i+1}" --date="{fecha_commit}"'
    os.system(commit_cmd)

print("✅ Commits generados con fechas anteriores correctamente.")
