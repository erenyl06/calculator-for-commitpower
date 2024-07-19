import os
import subprocess


def setup_sonar(sonarqube_server,key,name,login,password):
    # Define project and SonarQube properties
    sonar_properties = {
        'sonar.host.url': sonarqube_server,
        'sonar.projectKey': key,
        'sonar.projectName': name,
        'sonar.projectVersion': '1.0',
        'sonar.sources': '.',
        'sonar.login':login,
        'sonar.password':password
    }

    # Path to SonarScanner executable
    sonar_scanner_path = r'sonar-scanner-4.7.0.2747-linux/bin/sonar-scanner.bat'

    # Path to project directory
    project_dir = r'sonar-scanner-4.7.0.2747-linux/src/{projectName}'

    # Write sonar.properties file
    sonar_properties_file = os.path.join(project_dir, 'sonar-project.properties')
    with open(sonar_properties_file, 'w') as f:
        for key, value in sonar_properties.items():
            f.write(f'{key}={value}\n')

    print(f'Sonar properties written to: {sonar_properties_file}')

    # Run SonarScanner
    try:
        result = subprocess.run([sonar_scanner_path], cwd=project_dir, capture_output=True)
        print(result.stdout.decode('utf-8'))
        print(result.stderr.decode('utf-8'))

        if result.returncode == 0:
            print("SonarScanner analysis completed successfully.")
        else:
            print(f"SonarScanner analysis failed with return code {result.returncode}.")

    except Exception as e:
        print(f"Error running SonarScanner: {str(e)}")


if __name__ == "__main__":
    setup_sonar()
