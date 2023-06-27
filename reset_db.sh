#/bin/bash
# Borrar migraciones de cada carpeta

rm db.sqlite3
# Borrar migraciones de cada carpeta
for app in login suscripciones control_vehicular operaciones; do
    find ./$app/migrations -type f ! -name '__init__.py' -delete
done
./migrate.sh
