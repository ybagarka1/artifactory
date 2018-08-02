#!/usr/local/bin/python3.5
import requests
import json
from artifactory import ArtifactoryPath
aql = ArtifactoryPath("http://artifact.corp.continuum.net:8081/artifactory/", auth=('repluser', 'AP49A5SMDpZuQb7e9g7Tn5c45fbUfJkZMzmUSM'))
build_numbers = []
repo_name = 'dt-repo_its-portal-control'
artifacts = aql.aql("items.find", {"type":"any","repo":"{0}".format(repo_name),"modified":{"$before":"13mo"}})
#),"modified":{"$before":"3mo"}}) 
for element in artifacts:
	if element["path"] == "." and element["name"] != ".":
		build_numbers.append(int(element["name"]))

build_numbers.sort(key=int)
for i in build_numbers:
	print(i)
#	response = requests.delete('http://artifact.corp.continuum.net:8081/artifactory/api/build/{0}?buildNumbers=element["path"]&artifacts=1'.format(repo_name),auth=('repluser', 'AP49A5SMDpZuQb7e9g7Tn5c45fbUfJkZMzmUSM'))
	response = requests.delete('http://artifact.corp.continuum.net:8081/artifactory/{}/{}'.format(repo_name,i),auth=('repluser', 'AP49A5SMDpZuQb7e9g7Tn5c45fbUfJkZMzmUSM'))
	print(response)
