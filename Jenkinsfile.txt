pipeline {
    agent any  // This means the pipeline can run on any available Jenkins agent

    stages {
        // Stage 1: Build
        stage('Build') {
            steps {
                script {
                    // Install the dependencies specified in requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        // Stage 2: Test
        stage('Test') {
            steps {
                // Run Pytest tests
                sh 'pytest'
            }
        }

        // Stage 3: Docker Build
        stage('Docker Build') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile
                    docker.build('my-python-app:latest')
                }
            }
        }

        // Stage 4: Deploy to Minikube
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy the application using kubectl
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
