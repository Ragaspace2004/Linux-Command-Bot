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
- **Linux Man Pages** (for tuning the Gemini Model with exact details)

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
    pip install rich pyfiglet
    ```

3. **Run the Bot**:
    ```bash
    python3 Linux_Command_Bot.py
    ```

## Usage

### Command Lookup

**Example User Input**:```scan all the ports running on my network```
**Bot Output**:
```
Command: nmap
Short Description: Network scanner for identifying active hosts and services.
Syntax: nmap [options] [target]
Options:
    -sT: TCP SYN scan (default).
    -sU: UDP scan.
    -p: Specifies the ports to scan.
    -oN: Save the scan results to a normal output file.
    -oX: Save the scan results to an XML output file.
Category: Network scanning

Exact Command: nmap -T4 192.168.1.0/24
```

### Syntax Only

**Example User Input**:``` grep syntax```

**Bot Output**: ```grep [options] pattern [file] ```

### Options Only

**Example User Input**:```options for wget```

**Bot Output**:
```
-O: Specifies the output filename.
-q: Quiet mode (suppress output).
-b: Download in the background.
-c: Continue a partially downloaded file.
```

### Error Correction

**Example User Input**:
```
$ ping google.com    
ping: google.com: Temporary failure in name resolution
```
                                                          
**Bot Output**
```
Command: ping
Short Description: Sends ICMP echo requests to test network connectivity.
Syntax:  ping [options] [hostname or IP address]
Options:
    -c:  Specifies the number of pings to send.
    -t:  Continuously pings until interrupted.
    -i:  Specifies the interval between pings.
Category:  Network communication

Possible Causes:
    1. DNS Resolution Issues: The system might be unable to resolve the hostname "google.com" to an IP address.
    2. Network Connectivity: There might be a temporary network issue preventing the ping request from reaching its destination.

Troubleshooting Steps:
    1. Check DNS Configuration:  Ensure the system's DNS settings are correct (e.g., using `nslookup` or `dig`).
    2. Verify Network Connection: Check if the network is functioning by pinging other known hosts or websites.
    3. Temporary Network Glitch: Wait a short time and try the ping command again.

Alternative Command:
    Command:  host
    Short Description:  Performs DNS lookups.
    Syntax:  host [hostname]
    Options:
        -t A:  Performs an A record lookup.
        -t PTR:  Performs a PTR record lookup.
    Category:  DNS resolution
```
## Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

***MADE OUT OF PASSION AND TEAMWORK***
