import re

def validate_username(username):
    if not isinstance(username, str):
        return False
    if not (3 <= len(username) <= 16):
        return False
    # Must start with a letter or underscore, but not multiple underscores
    if not re.match(r'^[A-Za-z_]', username):
        return False
    if username.startswith("__"):
        return False
    # Disallow only underscores
    if username.count('_') == len(username):
        return False
    # After first character: letters, numbers, underscores
    if not re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', username):
        return False
    return True
