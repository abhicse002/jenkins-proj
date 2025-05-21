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
            echo 'Huarry...!! Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
            // mail to: 'admin@example.com',
            //     subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
            //     body: "Something went wrong with ${env.BUILD_URL}"
        }
    }
}
