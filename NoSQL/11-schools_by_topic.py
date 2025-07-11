#!/usr/bin/env python3
"""11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        topic (str): The topic to search for.

    Returns:
        list: List of documents (schools) that have the topic in their 'topics' list.
    """
    return list(mongo_collection.find({"topics": topic}))
