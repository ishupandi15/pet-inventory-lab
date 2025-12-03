import boto3
import json
from decimal import Decimal

# Helper function to convert Decimal to float
def convert_decimal(obj):
    if isinstance(obj, list):
        return [convert_decimal(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return float(obj)
    return obj

# DynamoDB and S3 setup
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
table = dynamodb.Table('PetInventory')

# Scan all items from DynamoDB
response = table.scan()
items = convert_decimal(response.get('Items', []))

# Define target bucket and file name — EDIT THIS to your bucket
bucket_name = "PUT-YOUR-BUCKET-NAME-HERE"
s3_key = "YourNameDynamoDbFolder-export/pets.json"

# Upload to S3
s3.put_object(
    Bucket=bucket_name,
    Key=s3_key,
    Body=json.dumps(items)
)

print(f"exported {len(items)} items to s3://{bucket_name}/{s3_key}")
