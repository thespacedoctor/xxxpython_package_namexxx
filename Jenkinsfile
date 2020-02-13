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
        always {
            slackSend message: "Build Finished - ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
            sh 'conda remove --yes -n ${BUILD_TAG}-p3 --all'
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
}
