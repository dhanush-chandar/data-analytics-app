pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Activate the virtual environment using bash
                    sh 'bash -c "source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run the tests using pytest
                    sh 'bash -c "source venv/bin/activate && pytest"'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    docker.build('my-python-app:latest')
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy to Minikube using kubectl
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
