pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('DOCKERHUB_CREDENTIALS')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t $DOCKERHUB_CREDENTIALS_USR/random-city-app:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push $DOCKERHUB_CREDENTIALS_USR/random-city-app:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}