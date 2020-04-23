// The failedStages variable is reused between stages
def failedStages=[]

//Declarative
pipeline {
  agent { label 'RaspberryPi' }
  options {
    timeout(time: 1, unit: 'HOURS')
  }
  
  stages {
    stage('Update the RaspberryPi') {
      steps {
        script {
          echo "Update the Rasbian OS..."
          sh "sudo apt-get --yes update"
          sh "sudo apt-get --yes upgrade"
          sh "sudo apt --yes autoremove"
          sh "sudo updatedb"
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
          //sh "sudo umount /media/pi/HDD_2T"
          //sh "sudo mount /dev/sda1 /media/pi/HDD_2T"
          //Mount command specific for the user pi 
          sh 'sudo mount -o uid=pi,gid=pi /dev/sda1 /home/pi/ExternalDisks/Toshiba2T/'
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
  post {
    always {
      script {
          if (currentBuild.currentResult == 'SUCCESS') {
            telegramSend(message: 'Hi Nikos, Your Raspberry Pi is updated!')
        } else if (currentBuild.currentResult == 'FAILURE') {
            telegramSend(message: "Hey Nikos, Something went wrong. Please check it here: \"${BUILD_URL}console\"")
        }
        }
      }
    }
}
