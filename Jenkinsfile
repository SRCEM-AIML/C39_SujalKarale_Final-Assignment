pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository
                git 'https://github.com/SRCEM-AIML/C39_SujalKarale_Final-Assignment.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                // Build Docker images for Flask and Django apps
                sh 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                // Start the containers
                sh 'docker-compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests for Flask and Django apps
                sh 'docker-compose exec flask-app pytest'
                sh 'docker-compose exec django-app python manage.py test'
            }
        }

        stage('Cleanup') {
            steps {
                // Stop and remove containers
                sh 'docker-compose down'
            }
        }
    }

    post {
        always {
            // Clean up unused Docker resources
            sh 'docker system prune -f'
        }
    }
}