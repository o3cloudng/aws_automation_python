# AWS AUTOMATION WITH PYTHON

## Project 1: Automatically tagging every EC2 instances with the name of the ec2 creator

![Automatically tag EC@ instance with the name of the owner](./img/auto_tag_ec2_python.png)

From the diagram above, the objective of this project.
1. When anyone creates an EC2 instance in our organisation
2. An EventBridge service is triggered which in turn runs a lambda function to extract all the information of the EC2 instance
3. Using some particula information from the data retrieved such as EC2 owner, the lambda function tagd the EC2 instance with the owner's name

## Create a Lambda function
![Lambda landing page](./img/lambda_home.png)

![Lambda basic info](./img/lambda_basic_info.png)

![Lambda](./img/lambda_1.png)

![Lambda python](./img/lambda_coding.png)

## Create Test
![Lambda function test](./img/lambda_blank_test.png)

## Create CloudTrial to identify logged in user
![CloudTrail](./img/cloudtrail/cloudtrail_home.png)

![CloudTrail](./img/cloudtrail/cloudtrail_general.png)

### Create S3 bucket & Role name

## Set Rules in the EventBridge
![EventBridge](./img/EventBridge/eventbrodge_home.png)

![EventBridge](./img/EventBridge/eventbridge_rule.png)

![EventBridge](./img/EventBridge/event_pattern.png)

![EventBridge](./img/EventBridge/event_pattern_2.png)

![EventBridge](./img/EventBridge/select_targets.png)
Here we select the lambda service and function

![EventBridge](./img/EventBridge/select_targets.png)

![EventBridge](./img/EventBridge/complete.png)
![EventBridge](./img/EventBridge/complete.png)
Complete

## Now the trigger has been added to our Lambda function
From:
![Lambda](./img/lambda_1.png)
To:
![EventBridge](./img/lambda_trigger.png)


## [Python Boto3 AWS Boto3 url ](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

[Automatically tag EC2 instance with the name of the owner](./auto_tag_ec2.py)