pipeline {
    agent any

    parameters {
        string(name: 'EXECUTOR_URL', defaultValue: '', description: 'Address of the Selenoid executor')
        string(name: 'APP_URL', defaultValue: '', description: 'Address of the OpenCart application')
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Browser to use for tests')
        string(name: 'BROWSER_VERSION', defaultValue: 'latest', description: 'Version of the browser')
        string(name: 'THREAD_COUNT', defaultValue: '1', description: 'Number of threads')
    }

    environment {
        ALLURE_RESULTS_DIRECTORY = 'allure-results'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/e-batanov/qa_study_ui', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                pytest --alluredir=${ALLURE_RESULTS_DIRECTORY} \
                       --executor_url=${params.EXECUTOR_URL} \
                       --app_url=${params.APP_URL} \
                       --browser=${params.BROWSER} \
                       --browser_version=${params.BROWSER_VERSION} \
                       --threads=${params.THREAD_COUNT}
                """
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS_DIRECTORY}"]]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/allure-results/*', allowEmptyArchive: true
            junit 'reports/*.xml'
        }
    }
}
