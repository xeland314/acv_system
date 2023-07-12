#!/bin/bash
# Borrar migraciones de cada carpeta

rm db.sqlite3
# Obtener una lista de todas las carpetas en el directorio actual
for app in $(ls -d */); do
    # Excluir las carpetas administracion_vehicular y venv
    if [ "$app" != "administracion_vehicular/" ] && [ "$app" != "venv/" ]; then
        # Borrar migraciones de la carpeta actual
        find ./$app/migrations -type f ! -name '__init__.py' -delete
    fi
done
./migrate.sh
