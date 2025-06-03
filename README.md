# 📚 Library App

A simple Flask-based web application for managing a library system, containerized with Docker and integrated with Jenkins for CI/CD.

## 🚀 Features

- **Flask Web Application**: Lightweight backend using Flask.
- **MySQL Database**: Persistent data storage with MySQL.
- **Dockerized**: Easy deployment using Docker and Docker Compose.
- **CI/CD with Jenkins**: Automated testing and deployment pipeline.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: MySQL
- **Containerization**: Docker, Docker Compose
- **CI/CD**: Jenkins
- **Testing**: Pytest

## 📂 Project Structure

```
library_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image for Flask app
├── compose.yml            # Docker Compose configuration
├── init.sql               # SQL script to initialize the database
├── wait_for_mysql.sh      # Wait script for MySQL readiness
├── Jenkinsfile            # Jenkins pipeline definition
├── test_app.py            # Pytest test cases
├── templates/             # HTML templates
└── static/                # Static files (CSS, JS)
```

## 🧪 Running Locally

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Evan28-png/library_app.git
   cd library_app
   ```

2. **Build and start the containers**:

   ```bash
   docker-compose up --build
   ```

3. **Access the application**:

   Open your browser and navigate to `http://localhost:5000`.

## 🧪 Running Tests

To execute the test suite:

```bash
docker-compose exec app pytest
```

*Note*: Replace `app` with the actual service name if different.

## ⚙️ Jenkins Pipeline

The project includes a `Jenkinsfile` for automating the build, test, and deployment processes:

- **Clone Repository**: Fetches the latest code.
- **Build Docker Containers**: Builds images using Docker Compose.
- **Start Application**: Launches the application in detached mode.
- **Run Tests**: Executes tests inside the Flask container.
- **Post-Deployment Check**: Verifies the application is running.
- **Clean Up**: Stops and removes containers (optional).

## ⚠️ Troubleshooting

- **Docker Not Found**: Ensure Docker CLI is installed inside the Jenkins container.
- **docker-compose Not Found**: Install Docker Compose inside the Jenkins container or use the Docker Compose plugin.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.
