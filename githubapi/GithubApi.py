import os
import requests

class GithubApi:
    def __init__(self, token):
        self.token = os.environ['GITHUB_TOKEN']
        self.base_url = "https://api.github.com"

    def get_user_info(self, username):
        url = f"{self.base_url}/users/{username}"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_repo_info(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_repo_issues(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()
    
    def get_repo_pull_requests(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_repo_contributors(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/contributors"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_repo_branches(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/branches"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commits(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_repo_releases(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/releases"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_repo_tags(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/tags"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_repo_languages(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/languages"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_topics(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/topics"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_license(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/license"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_repo_readme(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/readme"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_contents(self, owner, repo, path=""):
        url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_stats(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/stats/contributors"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_traffic(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/traffic/views"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_clones(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/traffic/clones"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_forks(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/forks"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_stargazers(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/stargazers"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_watchers(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/subscribers"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_repo_collaborators(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/collaborators"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_repo_issues_comments(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/comments"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_repo_pull_requests_comments(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls/comments"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit_comments(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/comments"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit(self, owner, repo, sha):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{sha}"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit_status(self, owner, repo, sha):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{sha}/status"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit_check_runs(self, owner, repo, sha):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{sha}/check-runs"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit_check_suites(self, owner, repo, sha):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{sha}/check-suites"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit_comments_for_commit(self, owner, repo, sha):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{sha}/comments"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit_statuses_for_commit(self, owner, repo, sha):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{sha}/statuses"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit_check_runs_for_commit(self, owner, repo, sha):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{sha}/check-runs"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_repo_commit_check_suites_for_commit(self, owner, repo, sha):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{sha}/check-suites"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

    def get_pull_request_info(self, owner, repo, pull_number):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls/{pull_number}"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    
    def get_pull_request_commits(self, owner, repo, pull_number):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls/{pull_number}/commits"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
    