README: Running Program with GUI using gui_env and pip install requirements.txt

This README will guide you through the process of running a Python program with a graphical user interface (GUI) using a virtual environment named gui_env and installing the necessary dependencies from a requirements.txt file.

Prerequisites:

Python is installed on your system. If not, download and install it from the official Python website (https://www.python.org/downloads/).
Ensure you have the necessary access rights to install packages on your system.
Step 1: Setup Virtual Environment

Open your terminal (Command Prompt on Windows or Terminal on macOS/Linux).
Change to the directory where your Python project is located. You can do this using the cd command (e.g., cd /path/to/your/project).
Step 2: Create a Virtual Environment (gui_env)

Run the following command to create a virtual environment named 'gui_env':
    python -m venv gui_env

Activate the virtual environment:

On Windows:
    gui_env\Scripts\activate
On macOS/Linux:
    source gui_env/bin/activate

Install Dependencies

With the virtual environment still active, navigate to the project directory (if not already there).
Use pip to install all the dependencies from the requirements.txt file:
    pip install -r requirements.txt

Ensure that your Python program, which includes GUI elements, is present in the project directory.
Run the program using Python:

    python eeg_gui.py