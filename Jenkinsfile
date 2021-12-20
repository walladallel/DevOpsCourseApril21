pipeline {
  agent any

  environment {
       REGISTRY = "<YOUR CONTAINER REGISTRY HERE>"
  }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            echo 'Starting to build docker image'
            script {
              sh ''
            }
        }
    }
  }
}


