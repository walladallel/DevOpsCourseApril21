pipeline {
  agent any

  environment {
      REGISTRY = "228281126655.dkr.ecr.us-east-1.amazonaws.com/jenkins-cr"
  }

  stages {
//     stage('Clone repository') {
//         steps{
//          sh 'git clone https://github.com/alonitac/DevOpsCourseApril21.git'
//         }
//      }
    stage('Build') {
      when { anyOf {branch "master";branch "dev";changeRequest() } }
      steps{
          sh '''
            IMG_NAME=simple-web-server:$BUILD_NUMBER
            echo "Building $IMG_NAME"
            docker build -t $IMG_NAME .
            docker tag $IMG_NAME ${REGISTRY}/$IMG_NAME
            docker push ${REGISTRY}/$IMG_NAME
          '''
      }
    }
  }
}


