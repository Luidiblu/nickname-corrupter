import argparse
import random
from typing import Dict, List


def create_substitution_dict() -> Dict[str, List[str]]:
    """
    Create a dictionary with custom character substitutions for each letter.
    """
    return {
        'a': ['ⱥ', 'ª', 'ą'],
        'b': ['ḅ', 'ᵬ', 'ƀ'],
        'c': ['₵', 'ċ', 'ȼ'],
        'd': ['ḏ', 'đ', 'ḍ'],
        'e': ['ₑ', 'ę', 'ḗ'],
        'f': ['ḟ', 'ƒ', 'ᵮ'],
        'g': ['ḡ', 'ğ', 'ǥ'],
        'h': ['ḫ', 'ħ', 'ḧ'],
        'i': ['Ϊ', 'ī', 'ḭ'],
        'j': ['ĵ', 'ǰ', 'ɉ'],
        'k': ['ḳ', 'ķ', 'ₖ'],
        'l': ['ḹ', 'ₗ', 'ļ'],
        'm': ['ṃ', 'ₘ', 'ɱ'],
        'n': ['⋸', 'ṋ', 'ń'],
        'o': ['ọ', 'ɵ', 'º'],
        'p': ['ṗ', 'ƥ', 'ₚ'],
        'q': ['ʠ', 'ĸ', 'ɋ'],
        'r': ['ṟ', 'ŗ', '₨'],
        's': ['Ƨ', 'ṧ', 'ŝ'],
        't': ['ₜ', 'ṱ', 'ŧ'],
        'u': ['ᵤ', 'ụ', 'ṳ'],
        'v': ['ᵛ', 'ṿ', 'ⱴ'],
        'w': ['ŵ', 'ẘ', 'ẉ'],
        'x': ['ẋ', 'Ӿ', 'ẍ'],
        'y': ['ẏ', 'ӯ', 'ɏ'],
        'z': ['ż', 'ẑ', '₮']
    }


def transform_text(text: str, substitutions: Dict[str, List[str]]) -> str:
    """
    Transform the input text using the provided substitution dictionary.
    """
    transformed = ''
    for char in text:
        lower_char = char.lower()
        if lower_char in substitutions:
            transformed_char = random.choice(substitutions[lower_char])
            # Randomly choose between uppercase and lowercase for the transformed character
            if random.choice([True, False]):
                transformed += transformed_char.upper()
            else:
                transformed += transformed_char
        else:
            transformed += char

    return transformed


def replace_spaces(text: str) -> str:
    """
    Replace spaces in the input text with underscores or hyphens.
    """
    replacements = ['_', '-']
    return ''.join(random.choice(replacements) if char == ' ' else char for char in text)


def add_random_underscore(text: str) -> str:
    """
    Add an underscore randomly at the beginning or end of the input text.
    """
    underscore_position = random.choice(['start', 'end'])
    if underscore_position == 'start':
        return '_' + text
    else:
        return text + '_'


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments and return an argparse.Namespace object.
    """
    parser = argparse.ArgumentParser(
        description="Transform text input with custom character substitutions, replacing spaces with underscores or hyphens, and adding a random underscore at the beginning or end of the text."
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file path. If specified, the transformed text will be saved to the provided file.",
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of nicknames to generate. Default is 1.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Create the substitution dictionary.
    substitutions = create_substitution_dict()

    # If an output file is specified, open it for writing.
    if args.output:
        output_file = open(args.output, "w", encoding="utf-8")

    # Get the input text from the user.
    input_text = input("Enter text to transform: ")

    # Generate the specified number of nicknames.
    for i in range(args.number):
        output_text = transform_text(input_text, substitutions)
        output_text = replace_spaces(output_text)
        output_text = add_random_underscore(output_text)

        # Write the transformed text to the output file or print it to the screen.
        if args.output:
            output_file.write(f"{output_text}\n\n")
        else:
            print(f"nick {i + 1}: {output_text}\n")

    # Close the output file if it was opened.
    if args.output:
        output_file.close()
        print(f"Transformed text(s) saved to {args.output}")


if __name__ == "__main__":
    main()
