pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'static-django-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        CONTAINER_NAME = 'static-django-container'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                sh 'docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run the Django tests using the test service defined in docker-compose.yml
                sh 'docker-compose run --rm test'
            }
            post {
                always {
                    // Generate and publish test reports
                    junit 'reports/*.xml'
                }
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                // Stop any existing container
                sh 'docker stop ${CONTAINER_NAME}-staging || true'
                sh 'docker rm ${CONTAINER_NAME}-staging || true'
                
                // Start the new container
                sh 'docker run -d --name ${CONTAINER_NAME}-staging -p 8001:8000 \
                    -e DEBUG=False \
                    -e SECRET_KEY=staging_secret_key \
                    -e ALLOWED_HOSTS=staging.example.com,localhost,127.0.0.1 \
                    ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                // Wait for manual approval
                input message: 'Deploy to production?', ok: 'Deploy'
                
                // Stop any existing container
                sh 'docker stop ${CONTAINER_NAME}-prod || true'
                sh 'docker rm ${CONTAINER_NAME}-prod || true'
                
                // Start the new container
                sh 'docker run -d --name ${CONTAINER_NAME}-prod -p 8000:8000 \
                    -e DEBUG=False \
                    -e SECRET_KEY=${PROD_SECRET_KEY} \
                    -e ALLOWED_HOSTS=example.com,www.example.com \
                    ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }
    }
    
    post {
        always {
            // Clean up older Docker images to save space
            sh 'docker image prune -f'
        }
        
        success {
            echo 'Pipeline completed successfully!'
        }
        
        failure {
            echo 'Pipeline failed!'
            // Send notification on failure
            mail to: 'admin@example.com',
                subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                body: "Something went wrong with ${env.BUILD_URL}"
        }
    }
}
