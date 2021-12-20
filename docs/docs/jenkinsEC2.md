# Provision Jenkins on EC2 Instance
## DevOps April 21
- Follow https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/
You may find `sudo amazon-linux-extras install epel -y` useful.
- Create Elastic IP and associate it to Jenkins instance
SSH to in VM, install Git, Docker, and Terraform
Add jenkins linux user the docker group, so Jenkins could run docker commands:
sudo usermod -a -G docker jenkins
Define docker to automatically start on boot by default:
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
Then restart jenkins by http://<ip>:8080/safeRestart
Fork https://github.com/alonitac/DevOpsCourseApril21.git
Visit you Jenkins server via http://<ip>:8080
Install Blue Ocean, Docker Pipeline Plugin plugins
In Blue Ocean, create a new pipeline by integrating your forked repo.
Make sure to issue an access token with at least the following permissions. Under Settings ->  Developer settings -> Personal access tokens -> (your jenkins token name)

In your forked repo settings, under Webhooks add the following endpoint:
http://<ip>:8080/github-webhook/
Make you you have the following configurations

Create a new PR to test whether an activity is triggered in your Jenkins server.
In your forked repo settings, under Branches add a new rule for master, as following:
Require a pull request before merging
Require status checks to pass before merging - add the following status check: continuous-integration/jenkins/pr-merge
Don’t allow administrators to push
Build Docker Images 

