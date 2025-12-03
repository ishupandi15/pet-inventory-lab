import boto3
from boto3.dynamodb.conditions import Key

# connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetInventory')

# Query for all pets of species "Dog"
response = table.query(
    KeyConditionExpression=Key('pet_species').eq('Dog')
)

items = response.get('Items', [])

# Display the results
print(f"Found {len(items)} item(s) with species 'Dog':")
for item in items:
    print(item)
