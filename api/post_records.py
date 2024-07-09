import json
from models.entrance_record import put_entrance_record
from lib.authorizer import authorize


def handler(event, context):
    print(event)
    if not authorize(event):
        return {"statusCode": 401}

    print("authorized")

    body = json.loads(event["body"])
    suica_id = body["suicaId"]
    record_type = body["recordType"]

    try:
        put_entrance_record(suica_id, record_type)

        response = {"statusCode": 201}

        return response
    except Exception as e:
        response = {"statusCode": 500, "body": json.dumps({"error": str(e)})}
        return response
