pipeline {
    agent any
    environment {
        VIRTUAL_ENV = 'venv'
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    if (!fileExists("${env.WORKSPACE}/${VIRTUAL_ENV}")) {
                        bat "python -m venv ${VIRTUAL_ENV}"
                    }
                    bat "source ${VIRTUAL_ENV}\Script\activate && pip install -r requirements.txt"
                }
            }
        }
        stage('Lint') {
            steps {
                script {
                    bat "source ${VIRTUAL_ENV}\Script\activate && flake8 app.py"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    bat "source ${VIRTUAL_ENV}\Script\activate && pytest"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo "Deploying application..."
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
