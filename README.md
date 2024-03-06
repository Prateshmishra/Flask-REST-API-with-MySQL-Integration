# Flask API with MySQL Integration

This project is a simple Flask API that integrates with a MySQL database to perform CRUD operations on an 'anime' table. It provides two endpoints for retrieving anime data and adding new anime entries to the database.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/flask-mysql-api.git
    ```

2. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the MySQL database settings in `app.py`:
    ```python
    # Database configuration
    DB_CONFIG = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "your_mysql_password",
        "database": "flask_api",
    }
    ```
    Replace `"your_mysql_password"` with your actual MySQL password.

## Usage

1. Start the Flask development server:
    ```bash
    python app.py
    ```

2. Access the API endpoints using a web browser or an API client like Postman:
    - `GET /get_data`: Retrieve all anime data from the database.
    - `POST /add_anime`: Add a new anime entry to the database.

## Endpoints

- `GET /get_data`: Retrieve all anime data from the database.
- `POST /add_anime`: Add a new anime entry to the database.

## Technologies Used

- **Flask**: Web framework for building the API.
- **Flask-RESTful**: Extension for creating REST APIs with Flask.
- **MySQL Connector/Python**: Python driver for connecting to MySQL databases.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
