pipeline {
  agent any
  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev";changeRequest() } }
        steps {
                echo 'Starting to build docker image'

                script {
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
}


