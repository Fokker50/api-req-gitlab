import requests

# Get all projects of the user
response = requests.get('https://gitlab.com/api/v4/users/raska4ka/projects')
my_projects = response.json()

print(my_projects)

for project in my_projects:
    print(f"Project name: {project['name']}\nProject URL: {project['web_url']}\n")
