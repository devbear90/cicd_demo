pipeline {
    agent any

    environment {
        DAG_PATH = "/opt/airflow/dags"
        AIRFLOW_CONTAINER = "airflow-webserver"
    }

    stages {
        stage('Clone Repository') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    git branch: 'main', url: 'https://github.com/devbear90/cicd_demo.git'
                }
            }
        }

        stage('Deploy DAGs') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "docker cp dags/. ${AIRFLOW_CONTAINER}:${DAG_PATH}/"
                }
            }
        }

        stage('Restart Airflow Scheduler') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "docker restart airflow-scheduler"
                }
            }
        }
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
