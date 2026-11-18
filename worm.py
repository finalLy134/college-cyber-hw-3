import os
import random
import shutil
import string
import sys

PREFIX = "sim_clone_"
MAX_COPIES = 5


# Returns the path of the currently running script or compiled executable
def get_self_path() -> str:
    if getattr(sys, "frozen", False):
        # Running as a compiled executable (.exe or .app binary)
        return sys.executable
    return os.path.abspath(__file__)


# Counts how many replicated copies already exist in the target directory
def count_existing_copies(directory: str) -> int:
    return sum(
        1
        for filename in os.listdir(directory)
        if filename.startswith(PREFIX)
    )


# Generates a random filename like 'sim_clone_a8f9k2.py' or '.exe'
def generate_random_name(extension: str) -> str:
    rand_id = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{PREFIX}{rand_id}{extension}"


def replicate() -> None:
    source_path = get_self_path()
    target_dir = os.path.dirname(source_path)
    _, extension = os.path.splitext(source_path)

    existing = count_existing_copies(target_dir)
    if existing >= MAX_COPIES:
        print(f"Limit reached ({existing}/{MAX_COPIES} copies exist). Stopping replication.")
        return

    new_filename = generate_random_name(extension)
    destination_path = os.path.join(target_dir, new_filename)

    # Ensure no name collision
    while os.path.exists(destination_path):
        new_filename = generate_random_name(extension)
        destination_path = os.path.join(target_dir, new_filename)

    shutil.copy2(source_path, destination_path)
    print(f"Created copy {existing + 1}/{MAX_COPIES}: {new_filename}")


if __name__ == "__main__":
    replicate()