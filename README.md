# Linux Command Bot

## Overview

**Linux Command Bot** is an intelligent command-line assistant designed to help Linux beginners learn and execute commands with ease. This bot interprets user needs, provides exact Linux commands, offers descriptions, syntaxes, options, and categorizes commands for better understanding. It can also correct erroneous commands or suggest alternatives.

## Key Features

- **Command Lookup**: Understand user requests and provide precise Linux commands with detailed descriptions.
- **Syntax and Options**: Display command syntax and options with descriptions.
- **Error Correction**: Suggest corrections or alternatives for erroneous commands.
- **Ease of Learning**: Simplify Linux command learning for beginners by offering comprehensive and precise information.

## Technologies Used

- **Gemini API**
- **Google AI Studio**
- **Python** (with libraries like `rich` and `pyfiglet` for CLI interface)
- **GitHub** (for version control and public repository)

## Installation

To install and run the Linux Command Bot, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Ragaspace2004/Linux-Command-Bot.git
    cd Linux-Command-Bot
    ```

2. **Install Dependencies**:
    ```bash
    pip install google-generativeai
    ```

3. **Run the Bot**:
    ```bash
    python3 Linux_Command_Bot.py
    ```

## Usage

### Command Lookup

**Example User Input**:


**Bot Output**:

| Command | Short Description           | Syntax                     | Options                               | Category           |
|---------|-----------------------------|----------------------------|---------------------------------------|--------------------|
| mkdir   | Creates a new directory     | `mkdir [OPTION] DIRECTORY` | `-p, --parents` Create parent directories as needed. | File Management   |

**Alternative Command**:

| Command | Short Description         | Syntax                  | Options                              | Category           |
|---------|---------------------------|-------------------------|--------------------------------------|--------------------|
| install | Create directories via `install` command | `install -d [OPTION] DIRECTORY` | `-v` Verbose mode. | File Management   |

### Syntax Only

**Example User Input**:

**Bot Output**:

### Options Only

**Example User Input**:

**Bot Output**:

| Option | Description                            |
|--------|----------------------------------------|
| `-p`   | Create parent directories as needed.   |
| `-v`   | Verbose mode.                          |
| `-m`   | Set file mode (as in chmod), not a=rwx - umask. |

### Error Correction

**Example User Input**:
**Bot Output**
*Error: Invalid option -z*
*Did you mean:
mkdir -p newfolder*

## Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue to discuss what you would like to change.


