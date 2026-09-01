import GithubApi

class GetPRInfo:
    def __init__(self, token):
        self.github_api = GithubApi.GithubApi(token)

    def get_pull_request_info(self, owner, repo):
        pull_requests = self.github_api.get_repo_pull_requests(owner, repo)
        pr_info_list = []
        for pr in pull_requests:
            pr_info = {
                "number": pr["number"],
                "title": pr["title"],
                "user": pr["user"]["login"],
                "state": pr["state"],
                "created_at": pr["created_at"],
                "updated_at": pr["updated_at"],
                "merged_at": pr.get("merged_at"),
                "closed_at": pr.get("closed_at"),
            }
            pr_info_list.append(pr_info)
        return pr_info_list