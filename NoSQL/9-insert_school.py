#!/usr/bin/env python3
"""9-insert_school.py"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into mongo_collection using kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        **kwargs: Key-value pairs to insert as the document.

    Returns:
        ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
