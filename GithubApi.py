#-----------------------------------------------------------------------------
# This example will show how to use Github api
# Using Python Github lib see who have mentioned my Username
# and Reply to all those posts
#-----------------------------------------------------------------------------



from github import Github

# User needs to create key at using his Github account
# and put this data in below strings


Token='your key'

#User inserts the Repo and User he wants to search for

User='apache'
Repo='spark'
g=Github(Token,per_page=100)
user=g.get_user(User)
repo=user.get_repo(Repo)
Rlist=repo.get_languages()
print(str(Rlist))


