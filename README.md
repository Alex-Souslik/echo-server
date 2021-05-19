# echo-server
Full deployment of a basic FastAPI server on EKS with Terraform and Helm

## Running

1. Setup AWS Cli & install Terraform
2. Create EKS cluster by running `terraform init && terrafom apply` inside the `terraform-eks` folder.
3. Configure kubectl by running the following command in the `terraform-eks` folder:
	`aws eks --region $(terraform output -raw region) update-kubeconfig --name $(terraform output -raw cluster_name)`
4. Deploy echo-server bt running `helm install echo-server .` inside chart folder.

## Notes

1. Dockerfile is included for ease of creating custom images.
2. The used image, along with number of replicas and service port can be changed inside the `chart\values.yaml` file.
