# CI/CD Pipeline using Git, Jenkins, Docker, and Kubernetes

##  Problem Statement

This project implements a Continuous Integration and Continuous Deployment (CI/CD) pipeline using Git, Jenkins, Docker, and Kubernetes. The pipeline automates the process of building artifacts upon code commits and deploying them to a Kubernetes cluster.

---

##  Objectives

- Automate build and deployment process  
- Reduce manual intervention  
- Ensure consistency and reliability  
- Implement scalable and secure CI/CD pipeline  

---

## Tools & Technologies Used

- Git & GitHub (Version Control)
- Jenkins (CI/CD Automation)
- Docker (Containerization)
- Kubernetes (Container Orchestration)
- Python (Flask Web Application)

---

##  CI/CD Workflow
- GitHub → Jenkins → Docker Build → Kubernetes Deployment → Service Exposure

---

## Pipeline Explanation

1. Jenkins monitors the GitHub repository using Poll SCM  
2. On detecting changes, Jenkins automatically triggers the pipeline  
3. Docker image is built from the application code  
4. Kubernetes deployment is updated with the new image version  
5. Application is deployed and accessible via service  

---

##  Jenkins Pipeline (Groovy Script)

```groovy
pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    parameters {
        string(name: 'REPO_URL', defaultValue: 'https://github.com/Savitri-koparde-hub/DevOps-Case-study.git')
        string(name: 'BRANCH', defaultValue: 'main')
    }

    environment {
        IMAGE_NAME = 'devops-portfolio'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: "${params.BRANCH}", url: "${params.REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withKubeConfig(credentialsId: 'kubeconfig-file') {
                    bat "kubectl apply -f k8s/"
                    bat "kubectl set image deployment/devops-app devops-container=%IMAGE_NAME%:%IMAGE_TAG%"
                }
            }
        }
    }

    post {
        success {
            echo "Deployment Successful"
        }
        failure {
            echo "Pipeline Failed"
        }
    }
}

## Screenshots

### Jenkins Pipeline
![Jenkins Pipeline](images/jenkins.png)

### Docker Build
![Docker](images/docker.png)

### Kubernetes Deployment
![Kubernetes](images/k8s.png)

###  Application Output
![Application](images/app.png)
