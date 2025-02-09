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
                sh """
                    # Töröld a régi DAG-okat
                    rm -rf ${env.DAG_SOURCE_DIR}/*
                    
                    # Másold át az új DAG-okat (abszolút útvonallal)
                    cp -r ${WORKSPACE}/dags/* ${env.DAG_SOURCE_DIR}/
                    
                    # Ellenőrzés
                    ls -la ${env.DAG_SOURCE_DIR}
                """
                }
            }
        }

        stage('Restart Scheduler') {
            steps {
                sh "docker restart airflow-scheduler"
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