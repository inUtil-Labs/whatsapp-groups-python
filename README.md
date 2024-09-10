# whatsapp-groups-python
This Python script allows you to list members of all WhatsApp groups you are a member of.


## Overview

This repository contains a Python script named `wgp.py` that allows you to fetch all members of the WhatsApp groups you are a member of. This README provides step-by-step instructions on how to set up and run the script.

## Prerequisites

Before you can run the script, you'll need to have Python 3.x installed on your system. You'll also need to install the required Python packages.

## Setup Instructions

### 1. Clone the Repository

Start by cloning this repository to your local machine. Open a terminal and run:

```bash
git clone https://github.com/inUtil-Labs/whatsapp-groups-python.git
cd whatsapp-groups-python
```

### 2. Create a Virtual Environment (Optional but Recommended)

Creating a virtual environment helps manage dependencies for your project. To create and activate a virtual environment, run:

```bash
python -m venv venv
```

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Required Packages

For this script, you need: `requests`, `time`, `json`, `Image`, `BytesIO`.


```bash
pip install requests pillow
```

### 4. Run the Script

You can now run the script with the following command:

```bash
python3 wgp.py
```

### 5. Follow the Prompts

The script will display a list of all WhatsApp groups and ask you to select one. Follow the on-screen prompts to interact with the script.

To run the script, you will need to get a valid api key to run this API: https://rapidapi.com/inutil-inutil-default/api/mywhinlite

## Example Usage

Here's an example of how to run the script:

```bash
python wgp.py
```

1. Enter a valid api-key.
2. The script will check if the mywhinlite instance is running, if not, it will render a QR code that will need to be scanned.
3. The script will list all available WhatsApp groups.
4. You will have to choose a group by entering the corresponding number.
5. The script will display all the members of the whatsapp group.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or issues, please open an issue on the GitHub repository.






