pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'bash -c "source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'bash -c "source venv/bin/activate && pytest"'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    // Use sudo if permission issues persist
                    sh 'sudo docker build -t data-analytics-app .'
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
