# Employee Management Dashboard

## Executive Summary
The Employee Management Dashboard is a comprehensive web-based application built with Python and Streamlit. It provides a centralized interface for managing employee data, offering functionalities ranging from basic CRUD (Create, Read, Update, Delete) operations to data visualization and statistical analysis. The application is designed to be lightweight, utilizing local JSON storage for data persistence, making it highly portable and easy to deploy.

## Architecture Overview
The application follows a modular architecture, separating the core application logic, user interface components (views), and utility functions.

- **Frontend/UI:** Built using **Streamlit**, providing an interactive and responsive dashboard experience directly from Python code.
- **Data Processing:** Uses **Pandas** for efficient data manipulation and analysis.
- **Storage:** Employs a local JSON file (`database.json`) for simple, file-based data persistence.
- **Visualization:** Utilizes **Matplotlib** for rendering statistical charts and graphs.

### Project Structure
```text
employee-management/
├── index.py               # Main application entry point and sidebar navigation
├── helper.py              # Utility functions (validation, data loading/saving, Excel exports)
├── database.json          # Local file-based database for storing employee records
├── requirement.txt        # Project dependencies
└── views/                 # UI components and page layouts
    ├── home.py            # Dashboard overview
    ├── employee_list.py   # Displaying the list of employees
    ├── add_employee.py    # Form for adding new employees
    ├── edit_delete.py     # Interface for modifying or removing employee records
    └── statistics.py      # Data visualization and statistical insights
```

## Core Components

### 1. Main Dashboard (`index.py`)
Serves as the entry point of the application. It configures the Streamlit page layout and implements a sidebar navigation system to seamlessly switch between different functional views.

### 2. Utility Helpers (`helper.py`)
Contains essential helper functions that support the main application:
- **Data Validation:** Regular expressions for validating emails and phone numbers.
- **Data Operations:** Functions for loading from and saving to the `database.json` file.
- **Business Logic:** Age calculation and unique ID generation based on employee attributes.
- **Export Capabilities:** Integration with `openpyxl` to create and write data to Excel spreadsheets.

### 3. Views (`views/`)
- **Dashboard (`home.py`):** Provides a high-level summary of the system.
- **Employee List (`employee_list.py`):** Renders a tabular view of all current employees.
- **Add Employee (`add_employee.py`):** Contains input forms to register new staff members, integrating validation rules from `helper.py`.
- **Edit & Delete (`edit_delete.py`):** Allows administrators to update existing employee information or remove records from the system.
- **Statistics (`statistics.py`):** Generates visual charts (using Matplotlib) to analyze employee demographics, such as salary distributions, department breakdowns, and age statistics.

## Tech Stack & Dependencies
The project relies on the following key Python libraries:
- **[Streamlit](https://streamlit.io/):** For building the interactive web application interface.
- **[Pandas](https://pandas.pydata.org/):** For robust data handling and manipulation.
- **[Matplotlib](https://matplotlib.org/):** For creating static, animated, and interactive visualizations.
- **[OpenPyXL](https://openpyxl.readthedocs.io/):** For reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.

## Installation & Setup

1. **Clone the repository or navigate to the project directory:**
   ```bash
   cd d:\python\employee-management
   ```

2. **Install the required dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirement.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run index.py
   ```
   The dashboard will automatically open in your default web browser.
