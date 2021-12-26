pipeline {
  agent any

  stages {
    stage('Terraform Init & Plan'){
        when { anyOf {branch "master";branch "dev";changeRequest()} }
        steps {
            sh '''
            if [ "$BRANCH_NAME" = "master" ] || [ "$CHANGE_TARGET" = "master" ]; then
                cd infra/prod
            else
                cd infra/dev
            fi

            # your code here

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
                # your code here
            '''
        }
    }
  }
}


