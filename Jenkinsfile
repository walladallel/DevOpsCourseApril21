pipeline {
  agent any

  environment {
       REGISTRY = "228281126655.dkr.ecr.us-east-1.amazonaws.com"
  }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            echo 'Starting to build docker image'
            echo 'Authenticating aws docker registry'
            sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $REGISTRY'
            // echo 'Building Docker image...'
            // sh 'docker build -t simple-flask-app .'

        }
    }
  }
}


