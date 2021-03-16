import requests
import json


""" retrive user's repositories and store in a list """
def retrive_repo(userId: str):
    repoList = list()
    if userId == '':
        return None
    userUrl = "https://api.github.com/users/" + userId + "/repos"
    proxies = { "http": None, "https": None}
    r = requests.get(userUrl, verify=False, proxies = proxies)
    for i in range(len(r.json())):
        repoList.append(r.json()[i]['name'])
    return repoList


""" retrive user's commits in the repository """
def retrive_commits(userId: str, repositoryName: str):
    if userId == '':
        return None
    commitNumber = 0
    repositoryUrl = "https://api.github.com/repos/" + userId + "/" + repositoryName+"/commits"
    proxies = { "http": None, "https": None}
    r = requests.get(repositoryUrl, verify=False, proxies = proxies)
    for i in range(len(r.json())):
        if r.json()[i]['commit']:
            commitNumber += 1
    return commitNumber


""" get the output """
def outputRepo(userId: str):
    repoList = retrive_repo(userId)
    for i in repoList:
        print(f"Repo: {i}  Number of commits: {retrive_commits(userId, i)}")


outputRepo('richkempinski')

