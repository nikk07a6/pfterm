# pfterm - Terminal for Punyforth Devices

A terminal application for interacting with Punyforth devices through serial communication.

## Description

pfterm is a command-line terminal application designed specifically for communicating with Punyforth devices. It provides a simple interface for serial communication with configurable baud rates and convenient hotkeys for common operations.

## Installation

```bash
# Add installation instructions here
```

## Usage

```bash
pfterm [-h] [--baudrate BAUDRATE] port
```

### Arguments

- `port`: Serial port to connect to (required)
- `--baudrate`: Baud rate for serial communication (default: 115200)
- `-h`: Display help message

### Hotkeys

| Key Combination | Action |
|----------------|---------|
| Ctrl+A | Input from file |
| Ctrl+Z | Hardware reset via RTS line |
| Ctrl+Q or Ctrl+E | Exit application |

## Features

- Serial communication with Punyforth devices
- Configurable baud rate
- File input capability
- Hardware reset functionality
- Simple and intuitive interface

## Requirements

- Python 3.x
- pyserial library

## License

[Add license information here]

## Contributing

[Add contribution guidelines here]

## Author

[Add author information here]
