#!/bin/bash

# Arquivo onde vamos guardar o contador
VERSION_FILE="version.txt"

# Se o ficheiro não existir, cria começando em 0
if [ ! -f "$VERSION_FILE" ]; then
    echo "0" > "$VERSION_FILE"
fi

# Lê o valor atual
VERSION=$(cat "$VERSION_FILE")

# Incrementa +1
NEW_VERSION=$((VERSION + 1))

# Salva o novo valor no ficheiro
echo "$NEW_VERSION" > "$VERSION_FILE"

# Faz commit com o número atualizado
git add -A
git commit -m "upd 0.0.$NEW_VERSION"
git push
