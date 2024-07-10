import boto3

dynamodb = boto3.resource('dynamodb')


def put_user(suica_id: str, name: str, email: str):
    table = dynamodb.Table('User')
    table.put_item(Item={
        'suica_id': suica_id,
        'name': name,
        'email': email
    })

def get_user(suica_id: str):
    table = dynamodb.Table('User')
    response = table.get_item(Key={'suica_id': suica_id})
    print(response)
    return response.get('Item', None)
