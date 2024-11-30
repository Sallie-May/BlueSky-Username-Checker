# Bluesky Handle Resolver

This Python script resolves the availability of Bluesky handles (e.g., `@handle.bsky.social`). It checks whether the handle is already taken or if it is available, using the Bluesky API.

## Features

- Resolves whether a handle is available or taken on Bluesky.
- Supports concurrent requests for faster handling resolution with threads.
- Default files: 
  - **Input file**: `handles.txt` (a list of handles to check).
  - **Output file**: `valid_handles.txt` (a list of valid handles).
- Configurable number of threads (default is 20).

## Requirements

- Python 3.x
- Install dependencies using `pip`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sallie-May/BlueSky-Username-Checker.git
   cd BlueSky-Username-Checker-main
Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
You can run the script either with default values or by specifying command-line arguments.

With Command-Line Arguments:
```bash
python script_name.py [input_file] [output_file] -t [threads]

input_file: The file containing the list of handles to check (default: handles.txt).
output_file: The file to store valid handles (default: valid_handles.txt).
-t [threads]: Number of threads for concurrent checking (default: 20).
```
Without Command-Line Arguments (Uses Defaults):
```bash
python main.py
```
This will use the default input file handles.txt, the output file valid_handles.txt, and prompt for the number of threads.

Example:
```bash
python script_name.py handles.txt valid_handles.txt -t 10
```

This will check the handles in handles.txt using 10 threads, and write the valid handles to valid_handles.txt.

### `requirements.txt`

```text
requests
termcolor
```
