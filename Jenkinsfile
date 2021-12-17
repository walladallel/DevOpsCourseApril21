pipeline {
    agent any
    stages {
        stage('TF init & validate') {
            when { anyOf {branch "master";branch "dev"} }
            steps {
                sh '''
                cd infra/${BRANCH_NAME}
                terraform init
                terraform validate
                '''
            }
        }
        stage('TF plan') {
            when { anyOf {branch "master";branch "dev"} }
            steps {
                sh '''
                cd infra/${BRANCH_NAME}
                terraform plan
                '''
            }
        }
        stage('TF apply') {
           when { anyOf {branch "master";branch "dev"} }
           steps {
               sh '''
               cd infra/${BRANCH_NAME}
               terraform apply -auto-approve
               '''
           }
        }
    }
}


