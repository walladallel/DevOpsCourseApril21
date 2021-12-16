pipeline {
  agent any

  environment {
      REGISTRY = "228281126655.dkr.ecr.us-east-1.amazonaws.com/jenkins-cr"
  }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev";changeRequest() } }
      steps{
        script {
          sh 'IMG_NAME=simple-web-server-$BRANCH_NAME:$BUILD_NUMBER'
          sh 'docker build -t $IMG_NAME .'
          sh 'docker tag $IMG_NAME ${REGISTRY}/$IMG_NAME'
          sh 'docker push ${REGISTRY}/$IMG_NAME'
        }
      }
    }
  }
}


