pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Activate the virtual environment and install dependencies
                    sh 'bash -c "source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Verify pytest is installed and available
                    sh 'bash -c "source venv/bin/activate && pip list"'
                    
                    // Run tests using pytest
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
