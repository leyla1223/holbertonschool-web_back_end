#!/usr/bin/env python3
"""8-all.py"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection to query.

    Returns:
        list: List of documents, or empty list if none found.
    """
    return list(mongo_collection.find())
