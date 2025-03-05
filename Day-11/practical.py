# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# URL to fetch pull requests from the GitHub API
api_url= "https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Make a GET request to fetch pull requests data from the GitHub API
response= requests.get(api_url)

# Convert the JSON response to a dictionary
complete_details= response.json()

# Iterate through each pull request and extract the creator's name
for element in range(len(complete_details)):
    # Display the PR creators
    print(complete_details[element]["user"]["login"])