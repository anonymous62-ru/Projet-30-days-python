import random
import string

def random_user_id():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=6))

print(random_user_id())
