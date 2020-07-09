`d-bug12` is both a Python api, and a command line interface for the Dbug-12 program flashed in Motorola's HC12 chips

d-bug12
========

## Installation

### From source

```bash
pip install .
```

### Manually

Although the recommended way to install is using Python's package installer, there is an installation script in case you don't have `pip` set up.

```bash
sudo ./install
```

## CLI usage

```bash
dbug12 [flags] <command>
```

```
usage: cli.py [-h] [-p PORT] <command> ...

positional arguments:
  <command>             cli.py <command> -h will show further usage and
                        arguments, if any. Available commands are:

    load                Load a compiled program into memory
    run                 Start execution from a specific point of memory
    monitor             Spawns a terminal that directly communicates with the
                        board
    get-registers       Display CPU registers
    erase-memory        Erase a section of memory
    get-memory          Display a section of memory

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  serial communication port accessed by the board.
                        Default: "/dev/ttyUSB0"
```

## Examples

Examples for the Python api can be found in [examples](examples).

## Compilation

A command line implementation of the HC12 compiler for Linux can be found at [68hc12-linux](https://github.com/mlndz28/68hc12-linux).