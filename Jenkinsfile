pipeline {
  agent any

   environment {
        REGISTRY = "228281126655.dkr.ecr.us-east-1.amazonaws.com"
    }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev";changeRequest() } }
        steps {
                echo 'Starting to build docker image'

                script {
                  sh '''
                  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $REGISTRY
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
}


