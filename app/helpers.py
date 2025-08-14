import random
import string
from typing import Literal, TypedDict


class BasicResponse(TypedDict):
    ''' A typed dictionary for the session-setup API '''
    error: Literal[1, 0]
    message: str


def generate_string(length: int, has_number: Literal[1, 0] = 0, has_blanks: Literal[1, 0] = 0, has_uppercase: Literal[1, 0] = 0, has_lowercase: Literal[1, 0] = 0):
    ''' Generate a random string of a specific length and desiring characters. '''

    character_set = ''
    if has_number == 1:
        character_set += string.digits
    if has_uppercase == 1:
        character_set += string.ascii_uppercase
    if has_lowercase == 1:
        character_set += string.ascii_lowercase
    if has_blanks == 1:
        character_set += ' '

    return ''.join(random.choice(character_set) for _ in range(length))
