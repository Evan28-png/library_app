pipeline {
    agent any

    environment {
       COMPOSE_PROJECT_NAME = "apptest"
       PWD = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone your GitHub repo (change URL to your repo)
                git url: 'https://github.com/Evan28-png/library_app.git', branch: 'testing'
            }
        }

        stage('Build & Run') {
            steps {
                // Run docker-compose commands in the repo root so init.sql is accessible
                dir('.') {
		    sh 'export PWD=$PWD'
                    sh 'docker-compose build'
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                // Placeholder for your tests
                echo 'Add your test commands here'
            }
        }
    }

    post {
        always {
            // Cleanup containers, volumes, networks to avoid leftovers
	    echo "waiting for 10 mins before cleanup"
	    sleep time: 600, unit: 'SECONDS'
	
            dir('.') {
                sh 'docker-compose down -v'
            }
        }
    }
}

