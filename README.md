# jenkins_streamlit_application

#Architectural Overview of Application -

https://github.com/NiveditaMShinde/jenkins_streamlit_application/assets/66831307/213ca3f0-2617-40e4-bb29-865827798405

#How does it work -
There are two main phases of the application -
1. Streamlit Application for Fertilizer Recommendation
2. Jenkins Pipeline with Amazon CodeDeploy

#Streamlit Application for Fertilizer Recommendation -
Step 1: Build an ML model for recommendation

Here,

Used dataset named 'Fertilizer_Prediction.csv', which has been available on Kaggle.

Used Random Forest Classifier Algorithm for Prediction.

Step 2: Create a Streamlit Application
By using basic stramlit, created a simple interface.

#Jenkins Pipeline with Amazon CodeDeploy
Step 1: Created GitHub Repository with Branch Protection Rule and Webhook Configuration to Jenkins Server.

Step 2: Created 2 IAM Roles - one is for Code Deploy to deploy resources on EC2 and another one is Instance Profile for EC2 instance to S3 access.

Step 3: Launched 2 EC2 instances to deploy Streamlit application.

Step 4: Used ECS service to implement the load balancing in case of heavy loads.

Step 5: Created an S3 bucket as Code Deploy pull the code revision from jenkins.

Step 6: Configured Code Deploy:
• Created an Application
• Created a Deployment Group

Step 7: Created a jenkins freestyle project

Step 8:  Push the streamlit application code to github to deploy the Application to the EC2 automatically.

#Demonstration Video of whole Process -
