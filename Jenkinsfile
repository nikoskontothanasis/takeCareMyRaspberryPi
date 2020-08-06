// The failedStages variable is reused between stages
def failedStages=[]

//Declarative
pipeline {
  agent { label 'RaspberryPi' }
  parameters {
    string(name: 'filepath', defaultValue: '', description: "Specify the file path to replace all with spaces with _")
    booleanParam(name: 'autoremove', defaultValue: false, description: 'Enable or disable the autremove command. The default is disable.')
    
  }
    
  options {
    timeout(time: 1, unit: 'HOURS')
  }
  
  stages {
  
    stage('Mount the external drives') {
      steps {
        script {
          echo "Mounting..."
          //Mount command specific for the user pi 
          // sh 'sudo mount -o uid=pi,gid=pi /dev/sda1 /home/pi/ExternalDisks/Toshiba2T/'
        }
      }
      post {
        failure {
          script { failedStages.add(STAGE_NAME) }
          echo "Failed at stage \"${STAGE_NAME}\" with unhandled exception."
        }
      }
    }
 
    stage('Update the RaspberryPi') {
      steps {
        script {
          echo "Update the Rasbian OS..."
          sh "sudo apt-get --yes update --allow-downgrades"
          sh "sudo apt-get --yes upgrade --allow-downgrades"
          //sh "sudo updatedb"
        }
      }
      post {
        failure {
          script { failedStages.add(STAGE_NAME) }
          echo "Failed at stage \"${STAGE_NAME}\" with unhandled exception."
        }
      }      
    }
    
    stage('Autoremove Command') {
      when {
        expression { params.autoremove == 'true' }
      }
      steps {
        script {
          echo "Execution of autoremove command..."
          echo "${params.autoremove}"
          sh "sudo apt --yes autoremove"
        }
      }
      post {
        failure {
          script { failedStages.add(STAGE_NAME) }
          echo "Failed at stage \"${STAGE_NAME}\" with unhandled exception."
        }
      }      
    }
    
    stage('Replace White-Spaces') {
      steps {
        script {
          echo "The replacement will take place on ${filepath}..."
          sh "sudo python scripts/replaceWhiteSpaceChar.py ${filepath}"
        }
      }
      post {
        failure {
          script { failedStages.add(STAGE_NAME) }
          echo "Failed at stage \"${STAGE_NAME}\" with unhandled exception."
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
            telegramSend(message: "Hey Nikos, Something went wrong on \"${STAGE_NAME}\". Please check it here: \"${BUILD_URL}console\"")
        }
        }
      }
    }
}
