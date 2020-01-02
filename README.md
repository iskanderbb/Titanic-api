
A simple python flask rest API configured with mysql database

using Docker-compose to create and test with docker desktop

using Kompose, reconfigure yaml files, add secret and deploy on kuberntes Desktop 

### Deploy on kubernetes Engine: 

use ansible for configuration as code to create a cluster with nodes 
and deploy the sample application 


## for testing 

 Download the repo 

 run the command  "docker-compose up"
 
 check the api on your browser "localhost:8001/ui" 
  
 Stop the running containers or end docker-compose by "docker-compose down"
 
 run the file conf_apply_kubernetes.ps1 to apply the configuration of kubernetes
 
 check the list of services
  
 check the api on your browser "localhost:8000/ui"
 
 
 GKE deployment:
 the service account json file "sherweb-poject-sa.json" is not pushed to this public repository for security reasons

 can be tested by modifying main files under vars folders and including sa json file with GKE admin role
 
 

