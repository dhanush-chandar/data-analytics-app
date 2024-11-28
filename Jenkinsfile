pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'

                    // Activate the virtual environment and install dependencies
                    sh 'bash -c "source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }

        stage('Run Tests') {
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
                    // Print the current directory to ensure correct context
                    sh 'pwd'

                    // List files to confirm the Dockerfile is present
                    sh 'ls -l'

                    // Change permissions on the Dockerfile (if needed)
                    sh 'chmod 644 Dockerfile'

                    // Build the Docker image
                    sh 'sudo /usr/bin/docker build -t data-analytics-app .'
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy to Minikube using kubectl
                    sh 'kubectl apply -f k8s/deployment.yaml --validate=false'
                }
            }
        }
    }
}
