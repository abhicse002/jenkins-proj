# Static Django Project

A simple static Django website with a modern frontend, dockerized for easy deployment and CI/CD integration.

## Features

- Responsive design with Bootstrap 5
- Modern UI with custom CSS and animations
- Static pages: Home, About, Contact
- Docker and Docker Compose support for easy deployment
- Jenkins pipeline for automated CI/CD
- Backend-focused Django tests

## Development Setup

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```
   python manage.py runserver
   ```

4. Access the site at http://localhost:8000

## Docker Deployment

### Using Docker Compose (Recommended)

1. Build and start the containers:
   ```
   docker-compose up -d
   ```

2. Access the site at http://localhost:8000

3. Stop the containers:
   ```
   docker-compose down
   ```

### Using Docker Directly

1. Build the Docker image:
   ```
   docker build -t static-django .
   ```

2. Run the container:
   ```
   docker run -p 8000:8000 static-django
   ```

3. Access the site at http://localhost:8000

## Jenkins CI/CD Pipeline

This project includes a Jenkinsfile that sets up a complete CI/CD pipeline. The pipeline automates building, testing, and deploying the application across different environments.

### Pipeline Stages

1. **Checkout**: Fetches the latest code from the repository
2. **Build Docker Image**: Creates a Docker image tagged with the build number
3. **Run Tests**: Executes the Django backend tests using Docker Compose
4. **Deploy to Staging**: Automatically deploys to staging environment when changes are pushed to the `develop` branch
5. **Deploy to Production**: Deploys to production with manual approval when changes are merged to the `main` branch

### Setting Up the Pipeline in Jenkins

1. In Jenkins, create a new Pipeline job
2. Configure Pipeline to use "Pipeline script from SCM"
3. Select your SCM (Git, etc.) and repository URL
4. Set the Script Path to "Jenkinsfile"
5. Save and run the pipeline

### Running Tests Manually

To run the Django tests locally using the same configuration as in the CI pipeline:

```
docker-compose run test
```

## Environment Variables

- `DEBUG`: Set to "False" in production (default: "True")
- `SECRET_KEY`: Django secret key (has default value, should be changed in production)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts (default: "localhost,127.0.0.1")
