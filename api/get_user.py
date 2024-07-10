import json
from models.user import get_user
from lib.authorizer import authorize


def handler(event, context):
    if not authorize(event):
        return {"statusCode": 401}

    suica_id = event['pathParameters']['suica_id']
    print(suica_id)

    try:
        user = get_user(suica_id)
        if user:
            response = {"statusCode": 200, "body": json.dumps(user)}
        else:
            response = {"statusCode": 404, "body": json.dumps({"error": "User not found"})}

        return response
    except Exception as e:
        response = {"statusCode": 500, "body": json.dumps({"error": str(e)})}
        return response
