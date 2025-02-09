pipeline {
    agent any

    // Környezeti változók helyesen definiálva
    environment {
        DAG_SOURCE_DIR = "/var/jenkins_dags"  // Ellenőrizd, hogy ez a helyes útvonal a konténerben!
        AIRFLOW_CONTAINER = "airflow-webserver"
    }

    stages {
        stage('Clone Repository') {
            steps {
                retry(3) {
                    checkout([ 
                        $class: 'GitSCM',
                        branches: [[name: 'main']],
                        extensions: [[$class: 'CleanCheckout']],
                        userRemoteConfigs: [[url: 'https://github.com/devbear90/cicd_demo.git']]
                    ])
                }
            }
        }

        stage('Deploy DAGs') {
            steps {
                script {
                    // DAG-ok másolása a volume-ba
                    sh """
                        rm -rf ${env.DAG_SOURCE_DIR}/*  # Használd a ${env.VÁLTOZÓ} szintaxist!
                        cp -r ./dags/* ${env.DAG_SOURCE_DIR}/
                        echo "✅ DAG-ok deployolva!"
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo "❌ CI/CD Sikertelen!"
        }
    }
}