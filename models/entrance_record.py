import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')


def put_entrance_record(suica_id: str, record_type: str):
    now = datetime.utcnow()

    table = dynamodb.Table('EntranceRecord')
    table.put_item(Item={
        'suica_id': suica_id,
        'record_type': record_type,
        'created_at': now.isoformat()
    })
