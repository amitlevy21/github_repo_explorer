def extract_repos_from_list(org_repo_list):
    repo_names = list()
    for repo in org_repo_list:
        repo_names.append(repo['full_name'])

    return repo_names
