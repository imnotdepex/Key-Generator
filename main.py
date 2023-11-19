import uuid
from github import Github
import json

def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def save_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def generate_key(length):
    random_key = str(uuid.uuid4())
    random_key = random_key.upper().replace("-", "")
    return random_key[:length]

def update_github_file(github_token, repo_owner, repo_name, file_path_in_repo, new_content):
    g = Github(github_token)
    repo = g.get_user(repo_owner).get_repo(repo_name)
    file = repo.get_contents(file_path_in_repo)
    commit_message = 'Update key.txt'
    repo.update_file(file_path_in_repo, commit_message, new_content, file.sha)

def main():
    config = load_config()

    key_length = config['key_length']
    save_to_github_flag = config['save_to_github']
    save_to_file_flag = config['save_to_file']
    github_token = config['github_token']
    repo_owner = config['repo_owner']
    repo_name = config['repo_name']
    file_path_in_repo = config['file_path_in_repo']
    output_file_path = config['output_file_path']

    generated_key = generate_key(key_length)
    print("Generated Key:", generated_key)

    if save_to_file_flag:
        save_to_file(output_file_path, generated_key)
        print("Key saved to file:", output_file_path)

    if save_to_github_flag:
        update_github_file(github_token, repo_owner, repo_name, file_path_in_repo, generated_key)
        print("Key updated on GitHub.")

if __name__ == "__main__":
    main()
