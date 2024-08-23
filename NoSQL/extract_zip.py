#!/usr/bin/env python3
import zipfile
import os

def extract_zip(file_path, extract_to):
    """Extrait un fichier ZIP vers un répertoire spécifié."""
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Fichiers extraits vers: {extract_to}")

if __name__ == "__main__":
    zip_file = 'dump.zip'
    extract_dir = 'dump'
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)
    extract_zip(zip_file, extract_dir)

