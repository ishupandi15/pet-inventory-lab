import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetInventory')

table.update_item(
    Key={
        'pet_species': 'Dog',
        'pet_id': 1
    },
    UpdateExpression='SET pet_name = :n',
    ExpressionAttributeValues={
        ':n': 'Orio'
    }
)

print("Pet name updated.")
