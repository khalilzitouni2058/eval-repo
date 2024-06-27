import git
def get_commit_info(repo_path, base_branch,pr_branch ):
    try:
        
        repo = git.Repo(repo_path)
        
        commit = repo.commit(base_branch)
        base_branch_commits = list(repo.iter_commits(base_branch))
        pr_branch_commits = list(repo.iter_commits(pr_branch))
        pr_commit = repo.commit(pr_branch)
        pr_merged = repo.is_ancestor(pr_commit, 'HEAD')
        
        commit_info = {
            'commit_id': commit.hexsha,
            'commit_title_body': commit.message.strip(),
            'author' : commit.author,
            'created_at': commit.authored_date,
            'updated_at': commit.committed_date,
            'closed': commit.repo.is_ancestor(commit, 'HEAD'),

        }
        commit_before_pr = base_branch_commits[0].hexsha if base_branch_commits else None
        commit_after_pr = pr_branch_commits[1].hexsha if pr_branch_commits else None
        number_of_commits = len(base_branch_commits)

        commit_pr_info = {
            'commit_before_pr' : commit_before_pr,
            'commit_after_pr' : commit_after_pr,
            'pr_merged': pr_merged,
            'number_of_commits':number_of_commits
        }
        
       

        return commit_info,commit_pr_info
    except Exception as e:
        
        print(f"Error getting commit ID: {e}")
        return None
    
if __name__ == "__main__":
    repo_path = '/Dracodes/eval-repo'
    base_branch  = 'main'  
    pr_branch = 'dev'
    

    commit_info,commit_pr_info = get_commit_info(repo_path, base_branch ,pr_branch)
    if commit_info:
        print("Commit Information:")
        print(f"Commit ID: {commit_info['commit_id']}")
        print(f"Commit Title: {commit_info['commit_title_body']}")
        print(f"Commit author: {commit_info['author']}")
        print(f"Commit created_at: {commit_info['created_at']}")
        print(f"Commit updated_at: {commit_info['updated_at']}")
        print(f"Commit closed: {commit_info['closed']}")
    print("***************")
    if commit_pr_info:
        print("Commit PR Information:")
        print(f"number_of_commits: {commit_pr_info['number_of_commits']}")
        print(f"commit_before_pr: {commit_pr_info['commit_before_pr']}")
        print(f"commit_after_pr: {commit_pr_info['commit_after_pr']}")
        print(f"PR Merged into HEAD: {commit_pr_info['pr_merged']}")

