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
This article explains how to migrate the AWS Email Notification System, which is currently functioning in HPC account. For the architecture of the notification system, please refer to this post: (https://cloudmaven.github.io/documentation/aws_cost_notification_system.html)

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

  - type in a name for the Lambda and choose the Runtime: Python 3.6
  
![pic0006](/documentation/images/aws/migrating_aws_cost_notification_system_006.png)

- Lambda function code:

the Lambda function code can be found here: [https://github.com/qjin2016/documentation/commit/d9e4461f7cd3f6e918b7be7bbb3994ef40a86d88]


Copy the Python code and paste it into the code section of Lambda page. Find the 'aws_access_key_id' and 'aws_secret_access_key' from the code. Replace their value with your keys. ATTENTION: NEVER PUT YOUR KEYS ON GITHUB OR ANY PUCLIC PLATFORM!!! Then find 'TopicArn' and replace its value with the TopicArn you just created in the SNS section.

This code also contains instructions of how to mute daily cost summary and send weekly cost summary only. Search 'if you do not wish to receive daily summary ...' from the code and you will find the instructions as part of the annotation.

After modifying Python code, go to the Configuration section.

In the 'Advanced settings' part, you can change Memory size and Timeout. The memory size is the memory allocated for running the Lambda function while the Timeout specifies the maximum time that the Lambda function will run. The default memory size is 128 MB, which should be enough for processing billing data. However, the default timeout setting is 10 seconds, which is insuffient for the current job. Increase it to 1 minute should be okay. If you need your Lambda to do a heavier job, make sure you further increase the memory size and timeout. But, Lambda is not designed for computationally expensive job, so keep in mind that one the reasons you go for Lambda is your computational task is lightweight.


Next, go to the 'Tags' part and tag your Lambda function properly according to the HPC policy.


Last but not least, the 'Monitoring' section. 

![pic0007](/documentation/images/aws/migrating_aws_cost_notification_system_007.png)

This section has a dashboard for you to keep track of your Lambda. To find logs of your Lambda, you can click the 'View logs in CloudWatch'. This will prompt you to the log files. You can see how your Lambda was executed in detail. It's a handly tool for debugging your Lambda code.


## Heads-up


## Next steps
The current notification system will parse raw billing data and send email notifications. It does not have the functionality to store the parsed information for future reference. It might be useful to keep the parsed information in an S3 bucket.

## Contact



{% include links.html %}
