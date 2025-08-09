import re

def is_valid_variable(nom):
    # ^ : début de chaîne
    # [a-zA-Z_]\w* : commence par lettre ou underscore, suivi de lettres/chiffres/underscores
    return bool(re.match(r'^[a-zA-Z_]\w*$', nom))

# Tests
print(is_valid_variable('first_name'))     # True
print(is_valid_variable('premier-nom'))    # False
print(is_valid_variable('1First_name'))    # False
print(is_valid_variable('firstname'))      # True
print(is_valid_variable('_privateVar'))    # True
print(is_valid_variable('nom variable'))   # False
