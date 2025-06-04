pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "apptest"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "📦 Cloning the Flask app repository..."
                git 'https://github.com/Evan28-png/library_app.git'
            }
        }

	stage('prepare init sql') {
	    steps {
		echo "copying init.sql to /temp"
		sh "cp init.sql /tmp/init.sql"
       	    }
	}	

 
        stage('Build Docker Containers') {
            steps {
                echo "🔨 Building Docker containers using docker-compose..."
                sh 'docker-compose build'
            }
        }

        stage('Start Application') {
            steps {
                echo "🚀 Starting the Flask app and its services in detached mode..."
                sh 'docker-compose up -d'
            }
        }

        stage('Post-Deployment Check') {
            steps {
                echo "🔍 Verifying that the Flask app is running..."
                sh 'curl -I http://localhost:5000 || echo "⚠️ App may not be responding"'
            }
        }

        stage('Clean Up (Optional)') {
            steps {
                echo "🧹 Cleaning up containers (you can disable this in production)..."
                sh 'docker-compose down'
            }
        }
  }

    post {
        always {
            echo "📋 Pipeline finished."
        }
        failure {
            echo "🚨 Something went wrong. Check the logs for details."
        }
    }
}

