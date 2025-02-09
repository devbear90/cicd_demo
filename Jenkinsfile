pipeline {
    agent any

    environment {
        DAG_PATH = "/opt/airflow/dags"
        AIRFLOW_CONTAINER = "airflow-webserver"
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    try {
                        checkout([
                            $class: 'GitSCM',
                            branches: [[name: 'main']],
                            extensions: [],
                            userRemoteConfigs: [[url: 'https://github.com/devbear90/cicd_demo.git']]
                        ])
                    } catch (err) {
                        echo "❌ Hiba a repository klónozásakor: ${err}"
                        currentBuild.result = 'FAILURE'
                        error("A build sikertelen")
                    }
                }
            }
        }

        // ... (a többi stage változatlan)
    }

    post {
        success {
            echo "✅ DAG Deployment Succeeded!"
        }
        failure {
            echo "❌ DAG Deployment Failed!"
        }
    }
}