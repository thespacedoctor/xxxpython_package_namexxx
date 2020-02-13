// JENKINS ENV VARS: https://jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables
String determineRepoName() {
    return scm.getUserRemoteConfigs()[0].getUrl().tokenize('/').last().split("\\.")[0]
}
def git_repo_name = determineRepoName()


pipeline {

    agent any

    // CHECK GITHUB EVERY 5 MINS MONDAY-FRIDAY
    // triggers {
    //     pollSCM('*/5 * * * 1-5')
    // }

    options {
        // skipDefaultCheckout(true)
        // KEEP THE 10 MOST RECENT BUILDS
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }
    // SOURCE ANACONDA
    environment {
      PATH="/var/lib/jenkins/anaconda/bin:$PATH"
    }

    stages {
        stage ("Code pull"){
            steps{
                checkout scm
            }
        }

        stage('Build conda python 3.7 environment') {
            steps {
                sh '''conda create --yes -n ${BUILD_TAG}-p3 python=3.7 pip
                      source activate ${BUILD_TAG}-p3 
                      python setup.py install
                    '''
            }
        }
        stage('Test conda python 3.7 environment') {
            steps {
                sh '''source activate ${BUILD_TAG}-p3 
                      pip list
                      which pip
                      which python
                    '''
            }
        }
    }
    post {
        // http://167.99.90.204:8080/blue/organizations/jenkins/${env.JOB_NAME}/${env.BUILD_NUMBER}/pipeline
        always {
            slackSend message: "${git_repo_name} ${env.NODE_NAME} Build Finished - ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.JENKINS_URL}/blue/organizations/jenkins/${env.JOB_NAME}/${env.BUILD_NUMBER}/pipeline|Open>)"
            sh 'conda remove --yes -n ${BUILD_TAG}-p3 --all'
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
}



