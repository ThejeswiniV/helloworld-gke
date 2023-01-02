# GKE-quick-start
Deploy hello world application in GKE
Python language

1. In this quickstart, you will store your container in Artifact Registry and deploy it to your cluster from the registry. 
Run the following command to create a repository named hello-repo in the same region as your cluster:

gcloud artifacts repositories create hello-repo \
    --project=PROJECT_ID \
    --repository-format=docker \
    --location=REGION \
    --description="Docker repository"
    
Replace the following values:

*PROJECT_ID* is your Google Cloud project ID
*REGION* is the location for the repository, such as us-west1. In the next section, you'll create the cluster for your container image deployment in the same region.

2. Build your container image using Cloud Build, which is similar to running docker build and docker push, but the build happens on Google Cloud:

gcloud builds submit \
  --tag REGION-docker.pkg.dev/PROJECT_ID/hello-repo/helloworld-gke .
  
3. Creating a GKE cluster
Choose the same region as your Artifact Registry repository.
"such as us-west1"

4.  In deployment.yaml file 
Replace the following values in your file:

$GCLOUD_PROJECT is your Google Cloud project ID:
$LOCATION is the repository location, such as us-west1.
