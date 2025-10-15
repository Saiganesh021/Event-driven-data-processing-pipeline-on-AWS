import json
import boto3
import os
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": "New event captured"
    }

    filename = f"raw-data/event_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=json.dumps(data))

    return {
        'statusCode': 200,
        'body': json.dumps('Data stored successfully!')
    }
