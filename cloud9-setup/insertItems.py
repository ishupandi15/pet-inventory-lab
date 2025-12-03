import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetInventory')

# Sample items
pets = [
    {'pet_species': 'Dog', 'pet_id': 1, 'pet_name': 'Buddy'},
    {'pet_species': 'Cat', 'pet_id': 2, 'pet_name': 'Whiskers'},
    {'pet_species': 'Bird', 'pet_id': 3, 'pet_name': 'Polly'}
]

# Insert each item
for pet in pets:
    table.put_item(Item=pet)

print("Items inserted successfully.")
