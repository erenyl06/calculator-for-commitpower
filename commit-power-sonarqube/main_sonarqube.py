# main.py

import yaml
from sonarqube import get_sonarqube_data
from repository import clone_and_move_repo
from run_sonar_scanner import setup_sonar

# Get the absolute path to the config.yaml file
base_path = os.path.dirname(__file__)
config_path = os.path.join(base_path, 'config.yaml')

# Load the YAML file
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

sonarqube_server = config['sonarqube_server']
project_key = config['project_key']
username = config['username']
password = config['password']
github_url = config['github_url']
new_location = config['new_location']

clone_and_move_repo(github_url, new_location)
setup_sonar(sonarqube_server,project_key,project_key,username,password)
# Get Quality Gate Status
quality_gate_url = f'{sonarqube_server}/api/qualitygates/project_status?projectKey={project_key}'
quality_gate_status = get_sonarqube_data(quality_gate_url, username, password)
if isinstance(quality_gate_status, dict):
    print("Quality Gate Status:", quality_gate_status)
elif isinstance(quality_gate_status, str):
    with open('quality_gate_status.html', 'w') as file:
        file.write(quality_gate_status)
    print("HTML content saved to quality_gate_status.html")

# Get Issues
issues_url = f'{sonarqube_server}/api/issues/search?projectKeys={project_key}'
issues = get_sonarqube_data(issues_url, username, password)
if isinstance(issues, dict):
    print("Issues:", issues)
elif isinstance(issues, str):
    with open('issues.html', 'w') as file:
        file.write(issues)
    print("HTML content saved to issues.html")

# Get Measures
measures_url = f'{sonarqube_server}/api/measures/component?component={project_key}&metricKeys=coverage,bugs,vulnerabilities,code_smells'
measures = get_sonarqube_data(measures_url, username, password)
if isinstance(measures, dict):
    print("Measures:", measures)
elif isinstance(measures, str):
    with open('measures.html', 'w') as file:
        file.write(measures)
    print("HTML content saved to measures.html")

# Clone and move repository

