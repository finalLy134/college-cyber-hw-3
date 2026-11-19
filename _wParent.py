# ~w~

from pathlib import Path

import shutil
import string
import random

FILE_NAME_PREFIX = '_w'
SIGNATURE_PREFIX = '# ~w~'

MAX_FILE_COUNT = 5


def generate_random_string(k=6):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=k))
    return random_string


def try_replicate(use_signature = True):
    files = [f for f in Path('.').iterdir() if f.is_file() and f.name.startswith(FILE_NAME_PREFIX)]
    
    if not use_signature:
        count = len(files)
    else:
        count = 0
        for file_name in files:
            with open(file_name, "r", encoding="utf-8") as file:
                first_x_chars = file.read(len(SIGNATURE_PREFIX))
                if first_x_chars == SIGNATURE_PREFIX:
                    count = count + 1
    
    if count >= MAX_FILE_COUNT:
        print(f"Can't replicate more than {MAX_FILE_COUNT}")
        return
    
    current_file = Path(__file__).resolve()
    new_name = FILE_NAME_PREFIX + generate_random_string() + current_file.suffix
    shutil.copy2(current_file, new_name)


if __name__ == '__main__':
    try_replicate()