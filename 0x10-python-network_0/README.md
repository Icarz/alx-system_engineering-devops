# 0x10. Python - Network #0

This project consists of a series of tasks aimed at exploring and understanding HTTP, APIs, and the various methods of interacting with them using Bash and Python.

## Tasks

### 0. cURL body size
- Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

### 1. cURL to the end
- Write a Bash script that sends a GET request to the URL, and displays the body of the response, but only if the response status code is 200.

### 2. cURL Method
- Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

### 3. cURL only methods
- Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

### 4. cURL headers
- Write a Bash script that sends a GET request to a URL with a custom header `X-School-User-Id: 98` and displays the body of the response.

### 5. cURL POST parameters
- Write a Bash script that sends a POST request to a URL with the parameters `email=test@gmail.com` and `subject="I will always be here for PLD"`, and displays the body of the response.

### 6. Find a peak
- Write a Python function that finds a peak in a list of unsorted integers. The function should follow an efficient algorithm (O(log n) or O(n)) to find a peak element.

## Requirements

- All Bash scripts must be exactly 3 lines long.
- All Python scripts should use `pycodestyle` for formatting.
- Each script should have a comment explaining its purpose.
- The Python function should be documented with a docstring explaining its purpose.

## Installation

To test the scripts, clone the repository and run them on an Ubuntu 20.04 LTS machine with Python 3.8.5. You can test each script by providing the necessary URL or input parameters.

```bash
git clone https://github.com/yourusername/alx-higher_level_programming.git
cd 0x10-python-network_0
