// JENKINS ENV VARS: https://jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables
// SLACK PLUGIN DOCS: https://jenkins.io/doc/pipeline/steps/slack/#slacksend-send-slack-message

@Library('thespacedoctor')_

def nice = "nice"

String determineBranchName() {
    return scm.getUserRemoteConfigs()[0].getUrl()
}
def git_branch_name = determineBranchName()

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
      REPO_NAME=setVars.repoName()
    }

    stages {
        stage ("Code pull"){
            steps{
                setVars.repoName()
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
        // http://167.99.90.204:8080/blue/organizations/jenkins/xxxpython_package_namexxx/detail/feature%2Fadding-jenkins-pipeline/12/pipeline
        // http://167.99.90.204:8080/blue/organizations/jenkins/xxxpython_package_namexxx/feature%2Fadding-jenkins-pipeline/12/pipeline/
        // http://167.99.90.204:8080/blue/organizations/jenkins/${env.JOB_NAME}/${env.BUILD_NUMBER}/pipeline
        // URL ENCODE BRANCH PLEASE: ${env.JENKINS_URL}/blue/organizations/jenkins/${git_repo_name}/${git_branch_name}/${env.BUILD_NUMBER}/pipeline
        always {
            // log.info("I can see you")
            sh 'echo ${nice}'
            slackSend message: "${env.BRANCH_NAME}\n ${env.REPO_NAME}\n ${env.NODE_NAME} Build Finished - ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.JENKINS_URL}/blue/organizations/jenkins/${env.JOB_NAME}/${env.BUILD_NUMBER}/pipeline|Open>)"
            sh 'conda remove --yes -n ${BUILD_TAG}-p3 --all'
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
}



