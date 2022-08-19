import json


def serialize(data, code: int = 200):
    return {
        "statusCode": code,
        "headers": {"Access-Control-Allow-Origin": '*'},
        "body": json.dumps(data)
    }
