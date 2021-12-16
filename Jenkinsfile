pipeline {
  agent any

  environment {
      REGISTRY = "228281126655.dkr.ecr.us-east-1.amazonaws.com/jenkins-cr"
  }

  stages {
    stage('Clone repository') {

          git clone https://github.com/alonitac/DevOpsCourseApril21.git
     }
    stage('Build') {
      when { anyOf {branch "master";branch "dev";changeRequest() } }
      steps{
          script {
            dockerImage = docker.build REGISTRY + ":$BUILD_NUMBER"
          }
//           sh '''
//             IMG_NAME=simple-web-server:$BUILD_NUMBER
//             echo "Building $IMG_NAME"
//             /Applications/Docker.app/Contents/Resources/bin/docker build -t $IMG_NAME .
//             /Applications/Docker.app/Contents/Resources/bin/docker tag $IMG_NAME ${REGISTRY}/$IMG_NAME
//             /Applications/Docker.app/Contents/Resources/bin/docker push ${REGISTRY}/$IMG_NAME
//           '''
      }
    }
  }
}


