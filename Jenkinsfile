pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
        PROJECT_NAME = 'django-static-site'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '>>> STEP: Checking out code from GitHub repository'
                // Checkout code from GitHub repository
                git url: 'https://github.com/abhicse002/jenkins-proj.git', branch: 'main'

                echo '>>> STEP: Displaying latest commit information'
                // Show latest commit info
                sh 'git log -1 --pretty=format:"%h - %an, %ar : %s"'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '>>> STEP: Setting up Python virtual environment and installing dependencies'
                // Create and activate a Python virtual environment
                sh '''
                    echo "Creating Python ${PYTHON_VERSION} virtual environment..."
                    python${PYTHON_VERSION} -m venv venv
                    . venv/bin/activate
                    echo "Upgrading pip..."
                    pip install --upgrade pip
                    echo "Installing project dependencies..."
                    pip install -r requirements.txt
                    echo "Python environment setup complete."
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                echo '>>> STEP: Collecting Django static files'
                // Collect static files
                sh '''
                    . venv/bin/activate
                    echo "Running collectstatic command..."
                    python manage.py collectstatic --noinput
                    echo "Static files collected successfully."
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '>>> STEP: Running Django tests'
                // Run Django tests using the custom test runner script
                sh '''
                    echo "Creating test runner script..."
                    cat > run_tests.py << 'EOF'
#!/usr/bin/env python
"""Test runner script to help with test discovery issues in Jenkins."""
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    # Set up Django environment
    os.environ['DJANGO_SETTINGS_MODULE'] = 'static_site.settings'
    django.setup()
    
    # Create test runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    
    # Run tests
    failures = test_runner.run_tests(["static_app"])
    sys.exit(bool(failures))
EOF
                    
                    echo "Making test runner executable..."
                    chmod +x run_tests.py
                    
                    echo "Activating virtual environment and running tests..."
                    . venv/bin/activate
                    ./run_tests.py
                    echo "Tests completed."
                '''
            }
        }

        stage('Deploy to Development') {
            steps {
                echo '>>> STEP: Deploying to development environment'
                sh '''
                    . venv/bin/activate
                    echo "Running pre-deployment checks..."
                    python manage.py check --deploy
                    echo "Pre-deployment checks completed."
                    echo "Development deployment ready."
                '''
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
            // mail to: 'abhicse002@gmail.com',
            //     subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
            //     body: "Something went wrong with ${env.BUILD_URL}"
        }
    }
}
