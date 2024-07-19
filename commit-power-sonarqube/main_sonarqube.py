# main.py

import yaml


from sonarqube import get_sonarqube_data
from repository import clone_and_move_repo
from run_sonar_scanner import setup_sonar
# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


sonarqube_server = config['sonarqube_server']
project_key = config['project_key']
username = config['username']
password = config['password']
github_url = config['github_url']
new_location = config['new_location']
sonar_path = config['sonar_path']

clone_and_move_repo(github_url, new_location)
setup_sonar(sonarqube_server,project_key,project_key,username,password,sonar_path,new_location)
# Get Quality Gate Status
quality_gate_url = f'{sonarqube_server}/api/qualitygates/project_status?projectKey={project_key}'
quality_gate_status = get_sonarqube_data(quality_gate_url, username, password)

if isinstance(quality_gate_status, dict):
    status = quality_gate_status.get('projectStatus', {}).get('status')
    conditions = quality_gate_status.get('projectStatus', {}).get('conditions', [])

    print("Quality Gate Status:", status)
    print("Conditions:")
    for condition in conditions:
        print(f"- {condition.get('metricKey')}: {condition.get('status')}")
elif isinstance(quality_gate_status, str):
    with open('quality_gate_status.html', 'w') as file:
        file.write(quality_gate_status)
    print("HTML content saved to quality_gate_status.html")


# Get Issues
issues_url = f'{sonarqube_server}/api/issues/search?projectKeys={project_key}&componentKeys={project_key}'
issues = get_sonarqube_data(issues_url, username, password)

if isinstance(issues, dict):
    total_issues = issues.get('total', 0)
    issues_list = issues.get('issues', [])

    print(f"Total Issues for project '{project_key}':", total_issues)
    print("Issues List:")
    for issue in issues_list:
        component = issue.get('component')
        line = issue.get('textRange', {}).get('startLine')
        message = issue.get('message')
        severity = issue.get('severity')
        print(f"- File: {component}, Line: {line}, Message: {message}, Severity: {severity}")
elif isinstance(issues, str):
    with open('issues.html', 'w') as file:
        file.write(issues)
    print("HTML content saved to issues.html")

# Get Measures
measures_url = f'{sonarqube_server}/api/measures/component?component={project_key}&metricKeys=coverage,line_coverage,bugs,reliability_rating,code_smells,sqale_index,sqale_rating,complexity,cognitive_complexity,duplicated_lines,duplicated_lines_density,classes'
measures = get_sonarqube_data(measures_url, username, password)

if isinstance(measures, dict):
    measures_data = measures.get('component', {}).get('measures', [])

    print("Measures:")
    for measure in measures_data:
        metric = measure.get('metric')
        value = measure.get('value')
        print(f"- {metric}: {value}")
elif isinstance(measures, str):
    with open('measures.html', 'w') as file:
        file.write(measures)
    print("HTML content saved to measures.html")
# Clone and move repository


