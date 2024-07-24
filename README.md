
# Session-Based Authentication Application

This is a Python application that implements session-based authentication. It provides functionalities for user login and session management. The application uses Flask for the backend.

## Project Structure
```
.
├── app.py
├── utils.py
└── templates
    ├── admin-login.html
    ├── doctor-login.html
    ├── index.html
    ├── pages.html
    └── patient-login.html
```
## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Harshyadav02/Session-Based-Authorization
    cd session-auth-app
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```sh
    python app.py
    ```

## Configuration

- **`app.py`**: The main application file where Flask routes and session management are defined.
- **`utils.py`**: Contains utility functions for the application.

## Templates

- **`admin-login.html`**: The login page for administrators.
- **`doctor-login.html`**: The login page for doctors.
- **`index.html`**: The main landing page after login.
- **`pages.html`**: A template for additional pages within the application.
- **`patient-login.html`**: The login page for patients.

