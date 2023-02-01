from github import Github

# using an access token
g = Github("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")

repo = g.get_repo("communitymedia/mediaphone")
open_issues = repo.get_issues(state = 'closed')
print(open_issues)
for issue in open_issues:
        print(issue)
        print(issue.labels)
