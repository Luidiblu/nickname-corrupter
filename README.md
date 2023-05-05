# Nickname Corrupter

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)

Nickname Corrupter is a simple yet creative command-line tool that transforms your text input with custom character substitutions, replaces spaces with underscores or hyphens, and adds a random underscore at the beginning or end of the text.

![Nickname Corrupter Banner](.github/banner.png)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/luidiblu/nickname-corrupter.git
```

2. Navigate to the repository folder:

```bash
cd nickname-corrupter
```

3. Ensure you have Python 3 installed on your system. You can check this by running:

```bash
python --version
```

## Usage

Run the script using the following command:

```bash
python corrupter.py "Your input text here"
```

To save the transformed text to a file, use the `-o` or `--output` option followed by the output file path:

```bash
python corrupter.py "Your input text here" -o output.txt
```

For more information on available options, run:

```bash
python corrupter.py --help
```

## Contribution

Contributions are welcome! If you have any ideas or suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
