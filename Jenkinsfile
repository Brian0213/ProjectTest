pipeline {
    agent any

    triggers {
        pollSCM('@midnight') // This schedules the pipeline to run every day at midnight.
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Brian0213/ProjectTest.git', credentialsId: '447bbc4c-d2c8-40c9-a6f3-61e5e8b936b6'
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
                            python testCases\\test_login.py
                        '''
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            pytest tests/
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            pytest tests/
                        '''
                    }
                }
            }
        }
    }
    post {
        always { 
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'reports', reportFiles: 'index.html', reportName: 'HTML Report'])
        }
    }
}

