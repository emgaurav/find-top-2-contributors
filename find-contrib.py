import requests

# Replace 'your_token_here' with your GitHub personal access token.
headers = {
    'Authorization': 'token your_token_here',
    'Accept': 'application/vnd.github.v3+json',
}

def get_top_contributors(repo):
    contributors_url = f'https://api.github.com/repos/{repo}/contributors'
    response = requests.get(contributors_url, headers=headers)
    
    if response.status_code == 200:
        contributors = response.json()
        if contributors:
            top_contributors = sorted(contributors, key=lambda x: x['contributions'], reverse=True)[:2]
            return ", ".join(contributor['login'] for contributor in top_contributors)
        else:
            return "No contributors found"
    elif response.status_code == 204:
        return "No content"
    else:
        return f"Error: Status Code {response.status_code}"

# Read repository list from a file
with open('repos.txt', 'r') as file:
    repos = [line.strip() for line in file if line.strip()]

for repo in repos:
    top_contributors = get_top_contributors(repo)
    print(f"Top contributors for {repo}: {top_contributors}")
