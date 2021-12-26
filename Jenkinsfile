pipeline {
  agent any

  stages {
    stage('Terraform Init & Plan'){
        when { anyOf {branch "master";branch "dev";changeRequest()} }
        steps {
            sh '''
            if [ "$BRANCH_NAME" = "master" || "$CHANGE_TARGET" = "master" ]; then
                cd infra/prod
            else
                cd infra/dev
            fi
            '''

            // YOUR CODE HERE


        }
    }

    stage('Terraform Apply'){
        when { anyOf {branch "master";branch "dev"} }
        input{
            message "Do you want to proceed for infrastructure provisioning?"
        }
        steps {
            sh '''

            cd infra/dev

            '''
            archiveArtifacts artifacts: 'tf_state/**/*.jar', fingerprint: true
        }
    }
  }
}


