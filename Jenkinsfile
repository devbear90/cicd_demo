pipeline {
    agent any

    environment {
        // Airflow konténer neve és DAG elérési út
        AIRFLOW_CONTAINER = "airflow-webserver"  // Ellenőrizd a konténer nevét!
        DAG_PATH = "/opt/airflow/dags"          // Ellenőrizd, hogy ez a helyes elérési út!
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Git repository klónozása (újrapróbálkozással)
                retry(3) {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'main']],
                        extensions: [[$class: 'CleanCheckout']], // Tiszta munkaterület
                        userRemoteConfigs: [[url: 'https://github.com/devbear90/cicd_demo.git']]
                    ])
                }
            }
        }

        stage('Deploy DAGs') {
            steps {
                script {
                    // DAG fájlok másolása az Airflow konténerbe
                    sh """
                        docker cp ./dags/ ${AIRFLOW_CONTAINER}:${DAG_PATH}/
                        echo "✅ DAG-ok sikeresen deployolva!"
                    """
                }
            }
        }

        stage('Restart Scheduler (Optional)') {
            steps {
                // Airflow scheduler újraindítása (ha szükséges)
                sh "docker restart airflow-scheduler"
            }
        }
    }

    post {
        always {
            cleanWs() // Munkaterület automatikus törlése
        }
        success {
            echo "🎉 CI/CD Sikeres!"
        }
        failure {
            echo "❌ CI/CD Sikertelen!"
        }
    }
}