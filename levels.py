import argparse
import eq_constants
import log_reader
import re
from datetime import datetime


def check_levels(log_file):
    data = log_file.read()
    level_regex = re.compile(r"\[(.+)\] You have gained a level! "
                             r"Welcome to level (\d{1,2})!")

    # only get the first time a level is dinged
    for match in re.findall(level_regex, data):
        if match[1] not in [x[1] for x in seen]:
            seen.append(match)

    zipped = zip(iter(seen), iter(seen[1:]))
    for lvl_info in zipped:
        level = int(lvl_info[0][1])
        time_start = datetime.strptime(lvl_info[0][0], eq_constants.DATE_FMT)
        time_end = datetime.strptime(lvl_info[1][0], eq_constants.DATE_FMT)
        print(f"{level}: {time_end - time_start}")


PARSER_DESC = "Check time it took to complete levels for a given character."
HELP_CHAR = "The character to check."

parser = argparse.ArgumentParser(description=PARSER_DESC)

parser.add_argument("character", type=str, help=HELP_CHAR)

args = parser.parse_args()

char_name = args.character.title()
seen = []

log_reader.handle(char_name, check_levels)
