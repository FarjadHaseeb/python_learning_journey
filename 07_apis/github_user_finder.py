import json
from urllib.request import urlopen

username = input("GitHub username: ")
url = f"https://api.github.com/users/{username}"

try:
    with urlopen(url) as response:
        data = json.load(response)
    print("Name:", data.get("name"))
    print("Public repos:", data.get("public_repos"))
    print("Followers:", data.get("followers"))
except Exception as e:
    print("Request failed:", e)
