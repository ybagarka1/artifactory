#!/usr/local/bin/python3.5
import requests
import json
from artifactory import ArtifactoryPath
aql = ArtifactoryPath("http://artifact.corp.continuum.net:8081/artifactory/", auth=('repluser', 'AP49A5SMDpZuQb7e9g7Tn5c45fbUfJkZMzmUSM'))
repo_name = 'dt-dev_its-portal-net' 
build_numbers = []
artifacts = aql.aql("items.find", {"type":"any","repo":"{0}".format(repo_name),"modified":{"$before":"8mo"}})
with open('data.json', 'w') as outfile:
	json.dump(artifacts, outfile)
for element in range(len(artifacts)):
	if (artifacts[element]["type"] == "folder" and artifacts[element]["name"] != "."):
		build_numbers.append(int(artifacts[element]["name"]))
build_numbers.sort(key=int)
for i in build_numbers:
	print(i)
#	response = requests.delete('http://artifact.corp.continuum.net:8081/artifactory/api/build/{}?buildNumbers={}&artifacts=1'.format(repo_name,i),auth=('repluser', 'AP49A5SMDpZuQb7e9g7Tn5c45fbUfJkZMzmUSM'))
	response = requests.delete('http://artifact.corp.continuum.net:8081/artifactory/{}/{}'.format(repo_name,i),auth=('repluser', 'AP49A5SMDpZuQb7e9g7Tn5c45fbUfJkZMzmUSM'))
	print(response)
