# GKE-quick-start
Deploy hello world application in GKE
Python language

Step:1 
Run this command in shell
 $ git clone https://github.com/ThejeswiniV/GKE-quick-start.git

Step:2
Go to "Artifact Registry" in console, click "create repository"
 1. Give Name as "hello-repo"
 2. Format as "Docker"
 3. Location type "Region"
    note: repository region and cluster region should be *same*
 4. Click create

Step:3
Create the cluster with same region for your container image deployment.
Build your container image using Cloud Build, which is similar to running docker build and docker push, but the build happens on Google Cloud:

gcloud builds submit \
  --tag REGION-docker.pkg.dev/PROJECT_ID/hello-repo/helloworld-gke .
  
3. Creating a GKE cluster
Choose the same region as your Artifact Registry repository.
"such as us-west1"

4.  In deployment.yaml file 
Replace the following values in your file:

$GCLOUD_PROJECT is your Google Cloud project ID:
$LOCATION is the repository location, such as us-west1.
