---
title: Migrating AWS Email Notification System
keywords: aws, lambda, sns
last_updated: September 27, 2017
tags: [AWS, Lambda, SNS, cost]
summary: "Migrating AWS Email Notification System to Other Account"
sidebar: mydoc_sidebar
permalink: migrating_aws_cost_notification_system.html
folder: aws
---

## Introduction
This article explains how to migrate the AWS Email Notification System, which is currently functioning in HPC account. For the architecture of the notification system, please refer to this post: https://cloudmaven.github.io/documentation/aws_cost_notification_system.html

## Step 1, Set Up Simple Notification Service (SNS)
During this step, we will create an SNS. The SNS will be able to send emails to subscribers. We will get a Topic ARN, which can be considered as an ID to the SNS. The Lambda service, which we will build up in the following steps, will use the Topic ARN to trigger the SNS.

- Log in AWS console, go to the SNS dashboard and then go further to the Topics section:
It doesn't matter which region you create your SNS, but it's a good idea to create you SNS and Lambda in the same region with the S3 bucket that syncs billing information. If SNS, Lambda and S3 are in different regions, there might be latency and addional cost because of longer distance communication across regions. It also makes your job easier to manage different services in the same region.

![pic0001](/documentation/images/aws/migrating_aws_cost_notification_system_001.png)

## Step 2, Create Lambda Service
The Lambda is the main component of the notification system. It listens to the S3 billing bucket update, parses cost information and triggers SNS to send email notifications.

- Go to the AWS Lambda dashboard and then move to the Functions section:

![pic0002](/documentation/images/aws/migrating_aws_cost_notification_system_002.png)

- Click the "Create function" button and then click the "Author from scratch" button:

![pic0003](/documentation/images/aws/migrating_aws_cost_notification_system_003.png)

- Add trigger:

![pic0004](/documentation/images/aws/migrating_aws_cost_notification_system_004.png)

![pic0005](/documentation/images/aws/migrating_aws_cost_notification_system_005.png)

- Configure function:

  - type in a name for the Lambda and set the Runtime to be Python 3.6
  
![pic0006](/documentation/images/aws/migrating_aws_cost_notification_system_006.png)

- Lambda function code:

the Lambda function code can be found here: 




## Heads-up


## Next steps
- aggregate total

## Contact



{% include links.html %}
