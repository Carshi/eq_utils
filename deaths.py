import argparse
import log_reader
import re


class KilledBy:
    def __init__(self, name, count):
        self.name = name
        self.count = count


def check_deaths(log_file):
    data = log_file.read()
    death_regex = re.compile(r"You have been slain by (.+)!")

    killed_by = re.findall(death_regex, data)
    kill_list = [KilledBy(d, killed_by.count(d))
                 for d in set(killed_by)]
    sorted_deaths = sorted(kill_list, key=lambda x: x.count, reverse=True)
    print(f"{char_name} has been killed by")

    for mob in sorted_deaths:
        times = f"time{'s' if mob.count != 1 else ''}"
        print(f"  {mob.name} {mob.count} {times}.")


PARSER_DESC = "Check deaths for a given character."
HELP_CHAR = "The character to check."

parser = argparse.ArgumentParser(description=PARSER_DESC)

parser.add_argument("character", type=str, help=HELP_CHAR)

args = parser.parse_args()

char_name = args.character.title()

log_reader.handle(char_name, check_deaths)
