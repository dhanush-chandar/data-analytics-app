pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Set up the virtual environment and install dependencies
                    sh 'python3 -m venv venv'  // Create a virtual environment
                    sh 'source venv/bin/activate && pip install -r requirements.txt'  // Activate and install dependencies
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run Pytest tests within the virtual environment
                    sh 'source venv/bin/activate && pytest'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    // Build the Docker image
                    docker.build('my-python-app:latest')
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy application using kubectl
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
