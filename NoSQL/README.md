this is the readme of the project NoSQL
# Projet NoSQL

Ce projet contient des scripts Python pour interagir avec une base de données MongoDB.

## Scripts

- `8-all.py` : Contient une fonction `list_all` qui récupère tous les documents d'une collection MongoDB.

## Dépendances

- Python 3.9
- PyMongo 4.8.0

## Utilisation

Pour utiliser les scripts, assurez-vous que `pymongo` est installé et que vous avez accès à une instance MongoDB.

Exemple d'utilisation de `8-all.py` :

```bash
#!/usr/bin/env python3
from pymongo import MongoClient
from 8-all import list_all

client = MongoClient('mongodb://127.0.0.1:27017')
school_collection = client.my_db.school
schools = list_all(school_collection)
for school in schools:
    print("[{}] {}".format(school.get('_id'), school.get('name')))
