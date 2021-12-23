# Provision Jenkins on EC2 Instance
1. Follow https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/

    You may find `sudo amazon-linux-extras install epel -y` useful.
2. Create Elastic IP and [associate it](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-associate-static-public-ip/) to Jenkins instance
3. SSH to in VM, install Git, [Docker](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html), and [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
4. Add jenkins linux user the docker group, so Jenkins could run docker commands:
   ```
   sudo usermod -a -G docker jenkins
   ```
   Define docker to automatically start on boot by default:
   ```shell
   sudo systemctl enable docker.service
   sudo systemctl enable containerd.service
   ```

   Then restart jenkins by http://<ip>:8080/safeRestart
5. Fork https://github.com/alonitac/DevOpsCourseApril21.git
6. Visit you Jenkins server via http://<ip>:8080
7. Install **Blue Ocean**, **Docker Pipeline Plugin** plugins
8. In Blue Ocean, create a new pipeline by integrating your forked repo.
9. Make sure to issue an access token with at least the following permissions. 

   *Under Settings ->  Developer settings -> Personal access tokens -> (your jenkins token name)*

10. In your forked repo settings, under Webhooks add the following endpoint:
http://<ip>:8080/github-webhook/
Make you you have the following configurations

11. Create a new PR to test whether an activity is triggered in your Jenkins server.
12. In your forked repo settings, under Branches add a new rule for master, as following:

    1. Require a pull request before merging
    2. Require status checks to pass before merging - add the following status check: continuous-integration/jenkins/pr-merge
    3. Don’t allow administrators to push

### Build Docker Images
We will dockerize a simple Flask web server. 
1. Make sure you understand `Dockefile` in branch `dev`
2. Build it locally (Docker should be installed)
```shell
# from repo working directory
docker build -t simple-flask-app:0.0.1 .
```

### Amazon ECR (Elastic container registry)
- In your Amazon web console, go to ECR
- Create a private repository with the **same name of your docker image**
- On the private repository page, click on "View push commands". It will help you to build you Jenkinsfile

### Building the Jenkinsfile
