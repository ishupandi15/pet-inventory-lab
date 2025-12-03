import boto3
import json
from decimal import Decimal

def convert_decimal(obj):
    if isinstance(obj, list):
        return [convert_decimal(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        if obj % 1 == 0:
            return int(obj)
        else:
            return float(obj)
    return obj

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetInventory')

response = table.scan()
items = response.get('Items', [])

print("All Pets in PetInventory:\n")
for item in convert_decimal(items):
    print(json.dumps(item, indent=4))
