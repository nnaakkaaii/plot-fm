import base64
import json
from enum import Enum


def serialize(data, code: int = 200):
    return {
        "statusCode": code,
        "headers": {"Access-Control-Allow-Origin": '*'},
        "body": json.dumps(data, ensure_ascii=False)
    }


class ContentType(Enum):
    Excel = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'


def encode(b: bytes, filename: str, content_type: ContentType):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': content_type.value,
            "Content-Disposition": f"attachment; filename={filename}",
        },
        'body': base64.b64encode(b).decode('utf-8'),
        'isBase64Encoded': True,
    }
