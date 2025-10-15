import boto3
import json
import os
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    report_data = {
        "date": datetime.utcnow().strftime('%Y-%m-%d'),
        "status": "Daily report generated successfully"
    }

    filename = f"reports/report_{datetime.utcnow().strftime('%Y%m%d')}.json"
    s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=json.dumps(report_data))

    return {
        'statusCode': 200,
        'body': json.dumps('Daily report generated successfully!')
    }
