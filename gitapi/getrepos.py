#!/usr/bin/env python3

import requests

def getRepos(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    
    print(response.json())

if __name__ == "__main__":
    getRepos("dgregory49")
