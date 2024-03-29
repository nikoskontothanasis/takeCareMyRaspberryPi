// The failedStages variable is reused between stages
def failedStages=[]

//Declarative
pipeline {
  agent { label 'RaspberryPi' }
  parameters {
    string(name: 'filepath', defaultValue: '/home/pi/Downloads/Torrents', description: "Specify the file path to replace all with spaces with _")
    //booleanParam(name: 'autoremove', defaultValue: '', description: 'Enable or disable the autremove command. The default is disable.')
    
  }
    
  options {
    timeout(time: 1, unit: 'HOURS')
  }
  
  stages {
  
    stage('Mount the external drives') {
       when {
        expression { params.mount == true }
      }
      steps {
        script {
          echo "Mounting..."
          //Mount command specific for the user pi 
          //sh 'sudo mount -o uid=pi,gid=pi /dev/sda1 /home/pi/ExternalDisks/Toshiba2T/'
          //sh 'sudo systemctl stop deluged.service'
          //sh 'sudo umount -l /home/pi/Shared/HDD'
          sh 'sudo mount -a'
          // sh 'sudo systemctl start deluged.service'
          //stop and start the deluged service in order to successfully un-mount and mount the disk, beacuse it uses it.
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
      when {
        expression { params.updateOS == true }
      }
      steps {
        script {
          echo "Update the Rasbian OS..."
          sh "sudo apt-get --yes update --allow-downgrades"
          sh "sudo apt-get -y --yes upgrade --allow-downgrades"
          sh "sudo apt-get autoclean"
         // sh "sudo updatedb"
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
        expression { params.autoremove == true }
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
    
    stage('Homebridge Update') {
      when {
        expression { params.homebridge == true }
      }
      steps {
        script {
          echo "Execution of Homebridge Update command..."
          sh "sudo npm install -g --unsafe-perm homebridge@latest"
          sh "sudo npm install -g --unsafe-perm homebridge-config-ui-x@latest"
        }
      }
      post {
        failure {
          script { failedStages.add(STAGE_NAME) }
          echo "Failed at stage \"${STAGE_NAME}\" with unhandled exception."
        }
      }      
    }
    
    stage('Pi-Hole Update') {
      when {
        expression { params.pihole == true }
      }
      steps {
        script {
          sh 'sudo pihole -up'
        }
      }
      post {
        failure {
          script { failedStages.add(STAGE_NAME) }
          echo "Failed at stage \"${STAGE_NAME}\" with unhandled exception."
        }
      }      
    }
    
    stage('Pi-Hole Maintenance') {
      when {
        expression { params.pihole == true }
      }
      steps {
        script {
          sh 'sudo systemctl restart pihole-FTL.service'
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
      when {
        expression { params.whitespace == true }
      }
      steps {
        script {
          echo "skip"
          echo "The replacement will take place on ${params.filepath}..."
          sh "sudo python scripts/replaceWhiteSpaceChar.py ${params.filepath}"
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
