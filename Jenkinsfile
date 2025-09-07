pipeline {
    agent any
    // agent {
    //     docker {
    //         image 'google/cloud-sdk:latest'
    //     }
    // }
    environment {
        DOCKER_HUB_REPO = "rajaramesh7410/vertexai-demo"
        DOCKER_HUB_CREDENTIALS_ID = "dockerhub-token"
        IMAGE_TAG = "v1"
        // IMAGE_TAG = "v${BUILD_NUMBER}"
    }
    stages {
        stage('Checkout Github') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/P-RajaRamesh/VertexAI-Service-Account-Auth-Demo.git']])
            }
        }        
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    dockerImage = docker.build("${DOCKER_HUB_REPO}:${IMAGE_TAG}")
                }
            }
        }
        stage('Push Image to DockerHub') {
            steps {
                script {
                    echo 'Pushing Docker image to DockerHub...'
                    docker.withRegistry('https://registry.hub.docker.com' , "${DOCKER_HUB_CREDENTIALS_ID}") {
                        dockerImage.push("${IMAGE_TAG}")
                    }
                }
            }
        }
        // stage('Update Deployment YAML with New Tag') {
        //     steps {
        //         script {
        //             sh """
        //             sed -i 's|image: rajaramesh7410/studybuddy:.*|image: rajaramesh7410/studybuddy:${IMAGE_TAG}|' manifests/deployment.yaml
        //             """
        //         }
        //     }
        // }
        // stage('Commit Updated YAML') {
        //     steps {
        //         script {
        //             withCredentials([usernamePassword(credentialsId: 'github-token', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
        //                 sh '''
        //                 git config user.name "P-RajaRamesh"
        //                 git config user.email "rajaramesh7410@gmail.com"
        //                 git add manifests/deployment.yaml
        //                 git commit -m "Update image tag to ${IMAGE_TAG}" || echo "No changes to commit"
        //                 git push https://${GIT_USER}:${GIT_PASS}@github.com/P-RajaRamesh/Study-Buddy-AI.git HEAD:main
        //                 '''
        //             }
        //         }
        //     }
        // }
        // stage('VertexAI Service Account Authentication...') {
        //     steps {
        //         script {
        //             withCredentials([file(credentialsId: 'gcp-service-account-key', variable: 'GCP_KEY')]) {
        //                 sh '''
        //                 export GOOGLE_APPLICATION_CREDENTIALS=$GCP_KEY
        //                 gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
        //                 '''
        //             }
        //         }
        //     }
        // }
        // stage('Install Kubectl & ArgoCD CLI Setup') {
        //     steps {
        //         sh '''
        //         echo 'installing Kubectl & ArgoCD cli...'
        //         curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
        //         chmod +x kubectl
        //         mv kubectl /usr/local/bin/kubectl
        //         curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
        //         chmod +x /usr/local/bin/argocd
        //         '''
        //     }
        // }
        // stage('Apply Kubernetes & Sync App with ArgoCD') {
        //     steps {
        //         script {
        //             kubeconfig(credentialsId: 'kubeconfig', serverUrl: 'https://192.168.49.2:8443') {
        //                 sh '''
        //                 argocd login 34.121.134.87:31704 --username admin --password $(kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d) --insecure
        //                 argocd app sync study
        //                 '''
        //             }
        //         }
        //     }
        // }
    }
}