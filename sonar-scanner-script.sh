#!/bin/bash

# Exit on failure
set -e

# Variables
SONAR_SCANNER_HOME='./sonar-scanner'

# Navigate to the directory to be scanned
cd $GITHUB_WORKSPACE

# Run SonarScanner
$SONAR_SCANNER_HOME/bin/sonar-scanner \
  -Dsonar.projectKey=my_project \
  -Dsonar.sources=. \
  -Dsonar.host.url= https://dead-84-51-5-150.ngrok-free.app
  -Dsonar.login=squ_e09d97410282ff1551ca4f62de1f40117daf87bd

# Process results as needed
