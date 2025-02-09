pipeline {
    agent any

    environment {
        DAG_PATH = "/opt/airflow/dags"
        AIRFLOW_CONTAINER = "airflow-webserver"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/devbear90/cicd_demo.git'
            }
        }

        stage('Deploy DAGs') {
            steps {
                script {
                    // Másolja a DAG-okat az Airflow konténerbe
                    sh "docker cp dags/. ${AIRFLOW_CONTAINER}:${DAG_PATH}/"
                }
            }
        }

        stage('Restart Airflow Scheduler') {
            steps {
                script {
                    // Újraindítja az Airflow Scheduler-t, hogy betöltse az új DAG-okat
                    sh "docker restart airflow-scheduler"
                }
            }
        }
    }
}
