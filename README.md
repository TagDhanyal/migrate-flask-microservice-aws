# Secured-Rest-Api
---

This solution uses Terraform to deliver a CodePipeline environment for a Python Flask API application on Amazon Elastic Container Service (ECS) using an Amazon Elastic Compute Cloud (EC2) launch type for the ECS service task definition.  The solution loads the codebase to AWS CodeCommit, leverages AWS CodeBuild to create the Docker image for the container, and uses AWS CodeDeploy to launch the ECS service and manage the solution deployment.    

# AWS Services Used
---

Let’s review the AWS services we are deploying with this project.

*CloudWatch* - [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) (Amazon CloudWatch) is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers to provide data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health.

*CodeBuild* - [AWS CodeBuild](https://aws.amazon.com/codebuild/) (AWS CodeBuild) is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.

*CodeCommit* - [AWS CodeCommit](https://aws.amazon.com/codecommit/) (AWS CodeCommit) is a secure, highly scalable, managed source control service that hosts private Git repositories.

*CodeDeploy* - [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) (AWS CodeDeploy) is a fully managed deployment service that automates software deployments to a variety of compute service such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers.

*CodePipeline* - [AWS CodePipeline](https://aws.amazon.com/codepipeline/) (AWS CodePipeline) is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates.

*Elastic Compute Cloud* - [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/) (Amazon EC2) offers the broadest and deepest compute platform, with over 500 instances and choice of the latest processor, storage, networking, operating system, and purchase model to help you best match the needs of your workload.

*Elastic Container Registry* - [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) (Amazon ECR) is a fully managed container registry offering high-performance hosting, so you can reliably deploy application images and artifacts anywhere.

*Elastic Container Service* - [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/) (Amazon ECS) is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications.

*Simple Storage Service* - [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/) (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.

*Virtual Private Cloud* - [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) (Amazon VPC) gives you full control over your virtual networking environment, including resource placement, connectivity, and security.

## Summary
---

This pattern is designed to provide a comprehensive deployment solution for ECS on EC2 using CodePipeline for blue green deployments including the following component configurations:

- Cloudwatch - alert metrics defined
- CodeBuild - the Docker container image is prepared and staged to ECR using CodeBuild
- CodeCommit - the GitHub repository code is copied and pushed to CodeCommit for use by CodePipeline
- CodeDeploy - deploys the containerized application prepared using CodeBuild
- CodePipeline - manages the software lifecycle by pulling from CodeCommit, building with CodeBuild, and deploying with CodeDeploy for a comprehensive CI/CD solution
- Elastic Compute Cloud - provides the resources, launch configuration, autoscaling group configuration for ECS, and the application autoscaling configuration for the ECS service
- Elastic Container Registry - provides a registry for application containers for use by ECS
- Elastic Container Service - provides an ECS cluster for use by CodeDeploy as a blue green deployment target
- Simple Storage Service - provides an object based storage bucket for use by CodePipeline to maintain the state of build artifacts used by the pipeline
- Virtual Private Cloud - provides networking, security, and connectivity for underlying infrastructure resources used to deliver the service


