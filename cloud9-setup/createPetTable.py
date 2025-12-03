import boto3

# Create DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create the table
table = dynamodb.create_table(
    TableName='PetInventory',
    AttributeDefinitions=[
        {
            'AttributeName': 'pet_species',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'pet_id',
            'AttributeType': 'N'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'pet_species',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'pet_id',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='PetInventory')

print("Table created successfully:", table.table_status)
