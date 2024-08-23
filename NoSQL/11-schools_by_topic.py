#!/usr/bin/env python3
"""Module pour récupérer les écoles ayant un sujet spécifique."""

def schools_by_topic(mongo_collection, topic):
    """
    Retourne une liste de tous les documents dans mongo_collection qui contiennent le sujet spécifié dans 'topic'.
    
    Args:
        mongo_collection: L'objet collection de pymongo dans lequel la recherche est effectuée.
        topic (str): Le sujet recherché.

    Returns:
        list: Liste des documents contenant le sujet spécifié dans leur champ 'topics'.
    """
    return list(mongo_collection.find({'topics': topic}))
