pipeline {
  agent { label 'RaspberryPi' }
  
  stages {
    stage('Update') {
      steps {
        script {
          echo "Update the Rasbian OS..."
          sh "sudo apt-get --yes update"
          sh "sudo apt-get --yes upgrade"
        }
      }
      post {
        failure {
          script { failedStages.add(STAGE_NAME) }
          echo "Failed at stage \"${STAGE_NAME}\" with unhandled exception. Check the end of the build log at ${BUILD_URL}console to view the error"
        }
      }      
    }
    
    stage('Mount the external drives') {
      steps {
        script {
          echo "Mounting..."
          sh "sudo mount /dev/sda1 /media/pi/HDD_2T"
        }
      }
      post {
        failure {
          script { failedStages.add(STAGE_NAME) }
          echo "Failed at stage \"${STAGE_NAME}\" with unhandled exception. Check the end of the build log at ${BUILD_URL}console to view the error"
        }
      }
    }
  }
}
