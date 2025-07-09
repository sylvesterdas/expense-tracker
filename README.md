# Expense Tracker

A simple command-line interface (CLI) tool to track your daily expenses. This project helps you practice Python fundamentals, including data structures, user input/output, and file handling.

## ✨ Features

  * **Add Expenses:** Record new expenditures with amount, description, and category.
  * **View Expenses:** Display a list of all recorded expenses.
  * **Data Persistence:** (Planned/Future Feature) Save and load expenses to/from a file, so your data isn't lost when the program closes.

## 🚀 Getting Started

Follow these steps to get the Expense Tracker up and running on your local machine.

### Prerequisites

  * Python 3.x installed on your system.

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone git@github.com:sylvesterdas/expense-tracker.git
    cd expense-tracker
    ```

2.  **Create a virtual environment:**
    It's good practice to use a virtual environment to manage project dependencies.

    ```bash
    python3 -m venv env
    ```

3.  **Activate the virtual environment:**

      * **On macOS/Linux:**
        ```bash
        source env/bin/activate
        ```
      * **On Windows (Command Prompt):**
        ```bash
        .\env\Scripts\activate.bat
        ```
      * **On Windows (PowerShell):**
        ```powershell
        .\env\Scripts\Activate.ps1
        ```

4.  **Install the project in editable mode:**
    This installs the necessary dependencies and sets up the `expense-tracker` command.

    ```bash
    pip install -e .
    ```

### Running the Application

Once setup, you can run the expense tracker using the command defined in `pyproject.toml`:

```bash
expense-tracker
```

## 💡 How to Use

Simply follow the on-screen menu prompts:

1.  Choose `1` to add a new expense.
2.  Choose `2` to view all your recorded expenses.
3.  Choose `3` to exit the application.