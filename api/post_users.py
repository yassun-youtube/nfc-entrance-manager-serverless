import json
from models.user import put_user
from lib.authorizer import authorize


def handler(event, context):
    if not authorize(event):
        return {"statusCode": 401}

    body = json.loads(event["body"])
    suica_id = body["suicaId"]
    name = body["name"]
    email = body["email"]

    try:
        put_user(suica_id, name, email)

        response = {"statusCode": 201}

        return response
    except Exception as e:
        response = {"statusCode": 500, "body": json.dumps({"error": str(e)})}
        return response
