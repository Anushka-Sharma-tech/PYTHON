# --------------------------------- COWSAY PACKAGE----------------------------------
import cowsay,sys
if len(sys.argv)==2:
    cowsay.cow("Hello, "+sys.argv[1])

import cowsay,sys
if len(sys.argv)==2:
    cowsay.trex("Hello, "+sys.argv[1])

#---------------------------------- REQUESTS PACKAGE AND JSON LIBRARY ------------------------------------
import requests,sys
import json
if len(sys.argv)>2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
print(json.dumps(response.json(),indent=2))

#---------------------------TO JUST GET THE SONG NAMES AND NOT ALL THE CRYPTIC DETAILS--------------------
import requests
import sys
import json
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])
o=response.json()
for result in o["results"]:
    print(result["trackName"])

