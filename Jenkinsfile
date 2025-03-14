// Jenkinsfile

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pulls code from Git repository
                git 'https://github.com/your-repo/python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the test using pytest
                sh 'pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                // Here you can deploy the app if needed (e.g., to a server or cloud)
                echo 'Deploying app...'
            }
        }
    }
}

