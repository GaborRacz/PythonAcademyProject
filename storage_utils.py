"""Various utils for making file-based data management easier."""

import os


def get_next_id(storage_path):
    """Calculate the next available identifier."""
    existing_ids = os.listdir(storage_path)
    integer_ids = []
    for i in existing_ids:
        try:
            current_id = int(i)
            integer_ids.append(current_id)
        except:
            pass
    try:
        last_id = max(integer_ids)
    except ValueError:
        last_id = 0
    return last_id + 1
