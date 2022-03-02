
**1) Create New Access Token**

Go to https://hub.docker.com/settings/security

New Access Token -> Access Token Description -> Access Type (Read, Write and Delete) -> Generate Token

Copy the Access Token

**2) Configure the Credentials with Jenkins**

Go to http://localhost:8080/credentials/store/system/domain/_/newCredentials

Username - <docker_hub_username>
ID - DOCKERHUB_CREDENTIALS
Password - <Access Token>

**3) Create a New Job**

Dashboard -> New Item -> Enter a Name -> Multi Branch -> Ok

Branch Sources -> Add Source -> Git -> Enter Git Repo Link (Repo Should be Public) -> Credentials -> Select the Credentials created before -> Save

**4) Check Status**

Click Status -> master -> Select Recent Build -> Console Output 

Then, Go to https://hub.docker.com/ and Ensure the images is pushed

**5) Pull & Run it in Local**

docker run <docker_hub_username>/random-city-app:latest