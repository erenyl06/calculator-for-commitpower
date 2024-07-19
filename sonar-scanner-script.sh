#!/bin/bash

# Exit on failure
set -e

# Variables
SONAR_SCANNER_HOME='./sonar-scanner'
SONAR_HOST_URL='https://dead-84-51-5-150.ngrok-free.app' # Your ngrok URL

# Navigate to the directory to be scanned
cd $GITHUB_WORKSPACE

# Run SonarScanner
$SONAR_SCANNER_HOME/bin/sonar-scanner -X \
  -Dsonar.projectKey=your_project_key \
  -Dsonar.sources=. \
  -Dsonar.host.url=$SONAR_HOST_URL \
  -Dsonar.login=$SONAR_TOKEN
