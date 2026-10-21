# pfterm - Terminal for Punyforth Devices

A command-line terminal for communicating with Punyforth devices over a serial connection. It supports interactive input, sending a file line by line, and resetting the device via RTS.

## Installation

Requires Python 3 and the packages listed in `requirements.txt` (`pyserial` and `prompt_toolkit`). Install them with:

```bash
python3 -m pip install -r requirements.txt
```

## Usage

```bash
python3 pfterm.py [--baudrate BAUDRATE] PORT
```

`PORT` is the serial port to connect to (for example, `/dev/ttyUSB0`). The baud rate defaults to `115200`.

Run `python3 pfterm.py --help` to see the command-line options.

### Hotkeys

| Key combination | Action |
|-----------------|--------|
| Ctrl+A | Enter a filename and send the file line by line |
| Ctrl+Z | Pulse the RTS line to reset the device |
| Ctrl+Q or Ctrl+E, then Enter | Exit the application |

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
