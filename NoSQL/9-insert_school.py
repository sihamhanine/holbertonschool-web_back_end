#!/usr/bin/env python3
"""Module pour insérer un nouveau document dans une collection MongoDB."""

def insert_school(mongo_collection, **kwargs):
    """
    Insère un nouveau document dans la collection mongo_collection avec les attributs spécifiés dans kwargs.
    
    Args:
        mongo_collection: L'objet collection de pymongo dans lequel insérer le document.
        **kwargs: Les champs et valeurs du document à insérer.
    
    Returns:
        L'identifiant (_id) du nouveau document inséré.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
