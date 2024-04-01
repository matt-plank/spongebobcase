import argparse
import random
import sys


def spongebob_case(text: str, prob_upper: float = 0.5) -> str:
    """Convert text into SpongeBob case.

    Args:
        text (str): The text to convert to SpongeBob case.
        prob_upper (float, optional): The probability of a character being made upper case. Defaults to 0.5.

    Returns:
        str: The SpongeBob case form of the input text.
    """
    result: str = ""

    for char in text.lower():
        if random.random() < prob_upper:
            result += char.upper()
            continue

        result += char

    return result


def main():
    """

    Usage

    cat file > spongebobcase
    spongebobcase -i "My text to spongebobify"

    """
    parser = argparse.ArgumentParser(description="Convert text to SpongeBob")
    parser.add_argument("-i", "--input", type=str, help="Text to convert to SpondeBob case")
    args = parser.parse_args()

    if args.input:
        converted_text = spongebob_case(args.input)
        print(converted_text)
        return

    converted_text = spongebob_case(sys.stdin.read())
    print(converted_text)


if __name__ == "__main__":
    main()
