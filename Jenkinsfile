pipeline {
  agent any

  environment {
      REGISTRY = "228281126655.dkr.ecr.us-east-1.amazonaws.com/jenkins-cr"
  }

  stages {
    stage('Clone repository') {
        steps{
         sh 'git clone https://github.com/alonitac/DevOpsCourseApril21.git'
        }
     }
    stage('Build') {
      when { anyOf {branch "master";branch "dev";changeRequest() } }
      steps{
          script {
            dockerImage = docker.build REGISTRY + ":$BUILD_NUMBER"
          }
      }
    }
  }
}


