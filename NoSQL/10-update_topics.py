#!/usr/bin/env python3
"""Module pour mettre à jour les sujets d'un document scolaire dans MongoDB."""

def update_topics(mongo_collection, name, topics):
    """
    Met à jour tous les documents de la collection mongo_collection dont le nom correspond à 'name',
    en remplaçant le champ 'topics' par la liste fournie dans 'topics'.
    
    Args:
        mongo_collection: L'objet collection de pymongo dans lequel les documents seront mis à jour.
        name (str): Le nom de l'école dont les documents doivent être mis à jour.
        topics (list): La liste des nouveaux sujets à définir pour les documents.

    Returns:
        None: La fonction met à jour les documents en place dans la collection et ne retourne rien.
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
