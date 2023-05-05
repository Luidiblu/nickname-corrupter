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
            transformed += random.choice(substitutions[lower_char])
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
        description="Transform text with custom character substitutions.")
    parser.add_argument("input_text", type=str,
                        help="Input text to be transformed.")
    parser.add_argument("-o", "--output", type=str,
                        help="Optional output file path. If provided, the transformed text will be saved to the specified file.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    input_text = args.input_text
    substitutions = create_substitution_dict()
    output_text = transform_text(input_text, substitutions)
    output_text = replace_spaces(output_text)
    output_text = add_random_underscore(output_text)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as output_file:
            output_file.write(output_text)
        print(f"Transformed text saved to {args.output}")
    else:
        print(output_text)


if __name__ == "__main__":
    main()
