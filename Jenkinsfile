pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
        PROJECT_NAME = 'django-static-site'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                git url: 'https://github.com/abhicse002/jenkins-proj.git', branch: 'main'

                // Show latest commit info
                sh 'git log -1 --pretty=format:"%h - %an, %ar : %s"'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create and activate a Python virtual environment
                sh '''
                    python${PYTHON_VERSION} -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                // Collect static files
                sh '''
                    . venv/bin/activate
                    python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run Django tests using the custom test runner script
                sh '''
                    . venv/bin/activate
                    # Make the test runner executable
                    chmod +x run_tests.py
                    # Run tests using the custom runner that properly sets up the environment
                    ./run_tests.py
                '''
            }
        }

        stage('Deploy to Development') {
            steps {
                echo 'Deploying to development environment...'
                sh '''
                    . venv/bin/activate
                    python manage.py check --deploy
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
