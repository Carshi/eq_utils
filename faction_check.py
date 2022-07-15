import argparse
import log_reader
import re


def check_faction(log_file):
    data = log_file.read()
    increases = 0
    decreases = 0
    faction_regex = fr"{args.faction} got (better|worse)"
    for match in re.findall(faction_regex, data, re.IGNORECASE):
        if match == "better":
            increases += 1
        else:
            decreases += 1
    print(f"{char_name} has {increases} positive hits with {args.faction}.")
    print(f"{char_name} has {decreases} negative hits with {args.faction}.")


PARSER_DESC = "Check faction hits for a given character and faction."
HELP_CHAR = "The character to check."
HELP_FACTION = "The name of the faction to check."

parser = argparse.ArgumentParser(description=PARSER_DESC)

parser.add_argument("character", type=str, help=HELP_CHAR)
parser.add_argument("faction", type=str, help=HELP_FACTION)

args = parser.parse_args()

char_name = args.character.title()

log_reader.handle(char_name, check_faction)
