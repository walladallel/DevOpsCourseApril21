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

            terraform init

            '''


        }
    }

    stage('Terraform Apply'){
        when { anyOf {branch "master";branch "dev"} }
        input{
            message "Do you want to proceed for infrastructure provisioning?"
        }
        steps {
            copyArtifacts filter: 'infra/dev/terraform.tfstate', fingerprintArtifacts: true, projectName: '${JOB_NAME}', selector: specific('${BUILD_NUMBER}')
            sh '''
            cd infra/dev
            terraform apply -auto-approve
            ls
            '''

            archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', fingerprint: true
        }
    }
  }
}


