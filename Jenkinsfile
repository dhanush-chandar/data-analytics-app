pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Create and activate a virtual environment, install dependencies
                    sh 'python3 -m venv venv'
                    sh 'bash -c "source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests using pytest
                    sh 'bash -c "source venv/bin/activate && pytest"'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    // Run Docker build with sudo (no password prompt)
                    sh 'sudo /usr/bin/docker build -t data-analytics-app .'
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy to Minikube
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
