import eq_constants
from os import path


def handle(char_name, func):
    try:
        log_path = path.join(eq_constants.LOG_PATH,
                             f"eqlog_{char_name}_project1999.txt")
        with open(log_path, "r", encoding="utf-8") as eq_log_file:
            func(eq_log_file)

    except FileNotFoundError:
        print(f"No log found for character '{char_name}'.")
