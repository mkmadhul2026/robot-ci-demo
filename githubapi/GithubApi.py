class githubapi:
    def __init__(self, token):
        self.token = token
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

    