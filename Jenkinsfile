pipeline {
  agent any
  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev";changeRequest() } }
        steps {
                echo 'Starting to build docker image'

                script {
                    def customImage = docker.build("my-image:${env.BUILD_ID}")
                    customImage.push()
                }
            }
    }
  }
}


