# Data Analytics Application CI/CD Pipeline

This project automates the deployment and testing of a data analytics application using a CI/CD pipeline powered by Jenkins, Docker, Kubernetes (via Minikube), and a variety of DevOps tools. The pipeline ensures smooth deployment and continuous integration for the data analytics app, making it more reliable and maintainable.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [Running Tests](#running-tests)
4. [Deployment](#deployment)
5. [Troubleshooting](#troubleshooting)
6. [License](#license)

---

## Project Overview

The project is designed to build and deploy a Python-based data analytics application, ensuring that code changes are continuously tested, built into Docker images, and deployed to Kubernetes via Minikube. It consists of the following stages:

- **Build Stage**: The Python environment is set up, and dependencies are installed.
- **Test Stage**: Unit tests are executed to ensure application correctness.
- **Docker Build Stage**: A Docker image is created for the app.
- **Deploy Stage**: The application is deployed to a local Kubernetes cluster (Minikube).

---

## Setup Instructions

### Prerequisites

1. **Jenkins Setup**: 
   - Jenkins should be installed and running with necessary plugins (e.g., Docker, Kubernetes, Git).
2. **Docker**: 
   - Ensure Docker is installed and configured on the Jenkins server.
3. **Minikube**:
   - Install Minikube for local Kubernetes cluster management.
4. **Python Environment**:
   - Python 3.x and pip installed.

### Steps to Run the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/data-analytics-app.git
   cd data-analytics-app
