# Key-Generator
Script Description: Key Generator and GitHub Updater

This script is designed for generating random keys and saving them both locally and in a remote GitHub repository. The script reads configuration parameters from the config.json file, including key length, flags for saving to a file and GitHub, GitHub token, and repository details. After generating a key, the script prints it to the console and, if required, saves it to the specified file and updates the file in the remote GitHub repository.

# Script Overview:
## Loading Configuration:
Loads configuration from the config.json file.
Returns a dictionary with configuration parameters.

## Saving to File:
Saves content to a file.
Takes a file path and content as input.

## Generating Key:
Generates a random key of a specified length.
Utilizes the uuid module to create a unique identifier, converts it to a string, and formats it.

## Updating GitHub File:
Updates the content of a file in the GitHub repository.
Uses the PyGithub library to interact with the GitHub API.

## Main Execution:
The main function where the core logic of the script is executed.
Loads configuration, generates a key, prints it to the console.
If flags for saving to a file or GitHub are set, respectively, saves the key to a file and updates it on GitHub.
# How to Use:
## config.json Explanation:

### key_length: Defines the length of the generated random key.

### save_to_github: A boolean flag indicating whether to save the generated key to a GitHub repository. true to enable, false to disable.

### save_to_file: A boolean flag indicating whether to save the generated key to a local file. true to enable, false to disable.

### github_token: GitHub personal access token. Required if save_to_github is set to true.

### repo_owner: GitHub repository owner's username or organization name. Required if save_to_github is set to true.

### repo_name: GitHub repository name. Required if save_to_github is set to true.
file_path_in_repo: Path to the file in the GitHub repository where the key will be stored. Required if save_to_github is set to true.
output_file_path: Path to the local file where the key will be saved. Required if save_to_file is set to true.

Adjust the values in config.json according to your needs. If you want to save the key to GitHub, ensure to provide a valid GitHub personal access token, repository owner, repository name, and file path in the repository. If you want to save the key to a local file, provide the path for output_file_path. Adjust the key_length based on your requirements. Set the flags save_to_github and save_to_file accordingly.
