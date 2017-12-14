from github import Github

Token='your key'
User='apache'
Repo='spark'
g=Github(Token,per_page=100)
user=g.get_user(User)
repo=user.get_repo(Repo)
Rlist=repo.get_languages()
print(str(Rlist))


