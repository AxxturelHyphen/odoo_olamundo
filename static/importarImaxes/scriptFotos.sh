#!/bin/bash

# Crear cabecera del CSV
echo '"id","foto"' > odoo_olamundo_informacion_fotos.csv

# Para cada foto, generar una fila que apunte a un registro de Información
for i in {1..3}; do
  B64=$(base64 -w0 "foto${i}.png")
  echo "\"odoo_olamundo.odoo_olamundo_informacion_${i}\",\"${B64}\"" >> odoo_olamundo_informacion_fotos.csv
done
