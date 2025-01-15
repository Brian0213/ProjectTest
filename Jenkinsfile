pipeline {
    agent any

    triggers {
        pollSCM('H/5 0 * * *') // This schedules the pipeline to run every day at midnight.
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '447bbc4c-d2c8-40c9-a6f3-61e5e8b936b6', url: 'https://github.com/Brian0213/ProjectTest.git']])
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            export PYTHONPATH=$WORKSPACE
                            python3 testCases/test_login.py
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            set PYTHONPATH=%WORKSPACE%
                            python3 testCases/test_login.py
                        '''
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'The job has been tested'
            }
        }
        post {
            always { 
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])
            }
        }
    }
}
