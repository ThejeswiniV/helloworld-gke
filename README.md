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

Step:4
Build your container image using Cloud Build, which is similar to running docker build and docker push, but the build happens on Google Cloud:
Now run this command in cloud shell.
 $ gcloud builds submit \
  --tag REGION-docker.pkg.dev/PROJECT_ID/hello-repo/helloworld-gke .
Replace the following values:
*PROJECT_ID* is your Google Cloud project ID
*REGION* is the location for the repository, such as us-west1.

Step:5
Once you create the cluster, deploy your container in "Workloads"
 1. Navigate to "workloads" 
 2. Click "Deploy"
 3. Specify container to "Existing container image"
 4. Select image path from *Artifact Registry*
 5. click Deploy
 
Step:6


