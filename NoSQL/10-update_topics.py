#!/usr/bin/env python3
"""10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all documents with the given school name.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
