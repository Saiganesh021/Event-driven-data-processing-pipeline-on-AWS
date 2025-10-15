# Event-driven-data-processing-pipeline-on-AWS
Fully automated event-driven data processing pipeline on AWS using Kinesis, Lambda, S3, and Athena. Infrastructure managed with Terraform and CI/CD implemented through GitHub Actions for continuous integration and deployment.
## Overview
This project implements an automated event-driven data processing pipeline using:

- AWS Lambda
- AWS S3
- AWS IAM
- Terraform (for infrastructure-as-code)
- GitHub Actions (optional for CI/CD)

## Architecture
1. `event_data_processor` Lambda stores incoming events to S3.
2. `daily_report_lambda` creates daily summaries in the same bucket.

## How to Deploy
- Run `terraform init`
- Run `terraform apply`
- Upload `lambda_function.zip` and `daily_report.zip` via Terraform

## Author
Sai Ganesh Paluri
