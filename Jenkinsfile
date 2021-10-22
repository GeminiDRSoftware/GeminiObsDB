#!/usr/bin/env groovy
/*
 * Jenkins Pipeline for GeminiObsDB
 *
 * by Bruno C. Quint
 * adapted for GeminiObsDB by Oliver Oberdorf
 *
 * Required Plug-ins:
 * - CloudBees File Leak Detector
 * - Cobertura Plug-in
 * - Warnings NG
 */

pipeline {
    agent any

    options { skipDefaultCheckout() }

    environment {
        PATH = "$JENKINS_HOME/anaconda3-dev-oly/bin:$PATH"
        CONDA_ENV_FILE = ".jenkins/conda_py3env_stable.yml"
        CONDA_ENV_NAME_DEPRECATED = "py3_stable"
        CONDA_ENV_NAME = "gemini_obs_db_pipeline_venv"
        TEST_IMAGE_PATH = "/tmp/archive_test_images"
        TEST_IMAGE_CACHE = "/tmp/cached_archive_test_images"
    }

    stages {
        stage ("Prepare"){

            steps{
                echo 'STARTED'

                checkout scm
            }

        }

        stage('Building Docker Containers') {
            steps {
                script {
                    def geminiobsdbimage = docker.build("gemini/geminiobsdb:jenkins", " -f docker/geminiobsdb-jenkins/Dockerfile .")
                    sh '''
                    echo "Clear existing Docker infrastructure to start with a blank slate"
                    docker network create geminiobsdb-jenkins || true
                    docker container rm geminiobsdb-jenkins || true
                    '''
                    def postgres = docker.image('postgres:12').withRun(" --network geminiobsdb-jenkins --name obsdata-jenkins -e POSTGRES_USER=fitsdata -e POSTGRES_PASSWORD=fitsdata -e POSTGRES_DB=fitsdata") { c ->
                        try {
                            docker.image('gemini/geminiobsdb:jenkins').inside(" -v reports:/data/reports -v /data/pytest_tmp:/tmp  --network geminiobsdb-jenkins") {
                                sh 'python3 /opt/FitsStorageDB/gemini_obs_db/scripts/create_tables.py --url postgresql://fitsdata:fitsdata@obsdata-jenkins/fitsdata'
                                echo "Running tests against docker containers"
                                sh  '''
                                    export STORAGE_ROOT=/tmp/jenkins_pytest/dataflow
                                    export GEMINI_OBS_DB_URL="postgresql://fitsdata:fitsdata@obsdata-jenkins/fitsdata"
                                    export TEST_IMAGE_PATH=/tmp/archive_test_images
                                    export TEST_IMAGE_CACHE=/tmp/cached_archive_test_images
                                    export CREATE_TEST_DB=False
                                    export PYTHONPATH=/opt/DRAGONS:/opt/FitsStorageDB
                                    mkdir -p /tmp/archive_test_images
                                    mkdir -p /tmp/cached_archive_test_images
                                    coverage run --omit "/usr/lib/*,/usr/local/*,/opt/DRAGONS/*" -m pytest /opt/FitsStorageDB/tests
                                    coverage report -m --fail-under=68
                                    '''
                            }
                        } catch (exc) {
                            throw exc
                        }
                    }
                }
            }
        }
    }
    post {
        always {
          junit (
            allowEmptyResults: true,
            testResults: 'reports/*_results.xml'
            )
          sh '''
             if [ -f dragons-repo.txt ]; then rm -rf `cat dragons-repo.txt`; fi
             docker rmi gemini/geminiobsdb:jenkins || true
             docker network rm geminiobsdb-jenkins || true
          '''
        }
        success {
            echo 'SUCCESSFUL'
        }
        failure {
            echo 'FAILED'
        }
    }
}
