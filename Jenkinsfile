pipeline {
    agent any

    environment {
        PYTHON_VENV = "${WORKSPACE}/venv" // Path to virtual environment
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv ${PYTHON_VENV}
                    source ${PYTHON_VENV}/bin/activate
                    pip install --upgrade pip
                    pip install pytest pytest-cov junit-xml
                '''
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Checking out code from Git repository...'
                checkout scm // Assumes repository is configured in Jenkins job
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests with pytest...'
                sh '''
                    source ${PYTHON_VENV}/bin/activate
                    pytest --junitxml=results.xml tests.py
                '''
            }
        }

        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results...'
                junit 'results.xml' // Publish JUnit-style XML report
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs() // Clean up workspace after build
        }
    }
}
