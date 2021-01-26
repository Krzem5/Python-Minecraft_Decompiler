import ntpath
import os
import requests
import urllib.request
import zipfile



TYPE="20w18a:server"



def _clone(url,fp):
	urllib.request.urlretrieve(url,fp)



print(f"Requesting release tree...")
json=[e for e in requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").json()["versions"] if e["id"]==TYPE.split(":")[0]][0]
print(f"Downloading {json['type']} {json['id']} ({json['releaseTime']})...")
json=requests.get(json["url"]).json()
print(f"{TYPE.split(':')[1].title()} url: {json['downloads'][TYPE.split(':')[1].lower()]['url']}...\n{TYPE.split(':')[1].title()} mapping url: {json['downloads'][TYPE.split(':')[1].lower()+'_mappings']['url']}...\nCreating temporary folder...")
if (ntpath.exists("tmp")):
	os.system("rm -rf tmp")
os.mkdir("tmp")
os.mkdir(f"tmp/{TYPE.split(':')[1].lower()}")
print(f"Downloading {TYPE.split(':')[1]}...")
_clone(json["downloads"][TYPE.split(":")[1].lower()]["url"],f"./tmp/{TYPE.split(':')[1].lower()}.jar")
print(f"Downloading {TYPE.split(':')[1]} mappings...")
_clone(json["downloads"][TYPE.split(":")[1].lower()+'_mappings']["url"],f"./tmp/{TYPE.split(':')[1].lower()+'_mappings'}.txt")
print("Getting jd-cli version...")
json=requests.get(requests.get("https://api.github.com/repos/kwart/jd-cmd/releases").json()[0]["assets_url"]).json()[1]
print(f"Downloading {json['name']}...")
_clone(json["browser_download_url"],"./tmp/jd-cli.zip")
print("Extracting jd-cli.jar...")
with zipfile.ZipFile("tmp/jd-cli.zip","r") as zf:
	zf.extract("jd-cli.jar",path="./tmp/")
os.system(f"java -jar tmp/jd-cli.jar -g INFO -od ./tmp/{TYPE.split(':')[1].lower()}/ ./tmp/{TYPE.split(':')[1].lower()}.jar")
print(f"Reading mappings from ./tmp/{TYPE.split(':')[1].lower()}-mappings.txt...")
m={}
with open(f"./tmp/{TYPE.split(':')[1].lower()}_mappings.txt","r") as f:
	f=f.read()
	for l in f.split("\n"):
		if (l[0]=="#"):
			continue
		else:
			pass
			###
