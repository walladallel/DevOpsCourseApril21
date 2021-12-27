pipeline {
  agent any

  stages {
    stage('Test infra only') {
        when { changeset "infra/**"}
        steps {
            sh "infra folder has been changed"
        }
    }

    stage('Terraform Init & Plan'){
        when { anyOf {branch "master";branch "dev";changeRequest()} }
        steps {
            sh '''
            if [ "$BRANCH_NAME" = "master" ] || [ "$CHANGE_TARGET" = "master" ]; then
                cd infra/prod
            else
                cd infra/dev
            fi
            '''
        }
    }

    stage('Terraform Apply'){
        when { anyOf {branch "master";branch "dev"} }
        input{
            message "Do you want to proceed for infrastructure provisioning?"
        }
        steps {
            sh '''
            '''
        }
    }
  }
}


