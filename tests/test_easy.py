"""
Test suite for easy deck

If needed, install pytest: pip install pytest

Then run the command: pytest
"""
import datetime
import os
import re
import sys
from io import StringIO

PLACE_HOLDER = "⚂"


def run_card(file_name, values=range(1, 21)):
    """Returns a list of printed lines"""
    file_path = os.path.normpath(
        os.path.join(
            sys.path[0], "../projects/programming-time/decks/easy", file_name + ".py"
        )
    )

    with open(file_path, "r", encoding="utf-8") as file:
        lines = []
        for line in file:
            line = line.rstrip()
            # remove blank and comment lines
            if line != "" and not re.match(r"^\s*#", line):
                lines.append(line)
        prog_text = "\n".join(lines)

    # replace PLACE_HOLDER symbols with actual values
    value_index = 0
    while prog_text.find(PLACE_HOLDER) != -1:
        prog_text = prog_text.replace(PLACE_HOLDER, str(values[value_index]), 1)
        value_index += 1

    # capture stdout output
    old_stdout = sys.stdout
    sys.stdout = my_stdout = StringIO()

    # pylint: disable = exec-used
    exec(prog_text)

    sys.stdout = old_stdout
    return my_stdout.getvalue().strip().split("\n")


def test_01():
    """gcd"""
    *_, output = run_card("01", [12, 16])
    assert int(output) == 4


def test_02():
    """Diffie-Hellman Key Exchange"""
    *_, output = run_card("02", [15, 7])

    # Example output: Shared Secret: 15 15
    match = re.search(r"(\d+).+?(\d+)", output)
    assert match is not None
    secret_ab = match.group(1)
    secret_ba = match.group(2)

    # shared secrets from both parties must match
    assert secret_ab == secret_ba


def test_03():
    """is_prime"""
    *_, output = run_card("03", [1])
    assert output == "not a prime"

    *_, output = run_card("03", [2])
    assert output == "prime"

    *_, output = run_card("03", [4])
    assert output == "not a prime"

    *_, output = run_card("03", [13])
    assert output == "prime"


def test_04():
    """RSA algorithm"""
    die = 17
    *_, output = run_card("04", [die])

    # recreate message as done in card
    message = 50 + 17
    decrypted = int(output)
    assert decrypted == message


def test_05():
    """sum & average"""
    *_, output = run_card("05", [10, 11, 12])
    average = float(output)
    assert average == 11


def test_06():
    """square root"""
    *_, output = run_card("06", [1])
    area = float(output)
    assert area == 32


def test_07():
    """remove() element from list"""
    *_, winner = run_card("07", [1])
    assert winner == "john"


def test_08():
    """quadrant"""
    *_, output = run_card("08", [11, 11])
    assert int(output) == 1

    *_, output = run_card("08", [11, 9])
    assert int(output) == 4

    *_, output = run_card("08", [9, 9])
    assert int(output) == 3

    *_, output = run_card("08", [9, 11])
    assert int(output) == 2

    *_, output = run_card("08", [10, 10])
    assert int(output) == 0


def test_09():
    """import"""
    now = datetime.datetime.now()
    meeting_time = 10
    *_, output = run_card("09", [meeting_time])

    expected = "on time" if now.minute < meeting_time else "you are late"
    assert output == expected


def test_10():
    """Reverse Polish Notation"""
    *_, output = run_card("10", [10, 11, 12])
    expected = (10 + 11) * 12
    assert float(output) == expected


def test_11():
    """encryption by transposition"""
    message = [1, 2, 3]
    *_, output = run_card("11", message)
    assert output == "nop"


# test_12(): not implemented due to package requirement


def test_13():
    """Haunted house"""
    *_, output = run_card("13", [1, 3])
    assert output == "phew! no ghost!"
