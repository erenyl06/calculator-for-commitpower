#!/bin/bash

# Exit on failure
set -e

# Variables
SONAR_SCANNER_HOME='C:\sonar-scanner-6.1.0.4477-windows-x64'

# Navigate to the directory to be scanned
cd $GITHUB_WORKSPACE

# Run SonarScanner
$SONAR_SCANNER_HOME/bin/sonar-scanner \
  -Dsonar.projectKey=my_project \
  -Dsonar.sources=. \
  -Dsonar.host.url=http:\\localhost:9000
  -Dsonar.login=squ_e09d97410282ff1551ca4f62de1f40117daf87bd

# Process results as needed
