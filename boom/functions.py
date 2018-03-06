"""
Functions
"""

import uuid
import random


def get_uuid_list(number, length):
    """
    Returns a list of "sentences" of uuids of
    random length.

    Parameters:
    number       the number of sentences to generate
    length       the maximum length of a sentence
    """

    utterances = []

    for i in range(0, number):

        utterance = []
        for j in range(1, random.randint(2, length)):
            utterance.append(uuid.uuid4().hex)
        utterances.append(" ".join(utterance))

    return utterances


def maybe_append_query_string(url, query_name, query_value):
    """
    If the query_name is present, adds the
    query string to the URL, filling in the
    query_value.
    """

    if query_name:
        url = "{}?{}={}".format(url, query_name, query_value)

    return url

