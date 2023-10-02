import boto3

dynamodb = boto3.client("dyanmodb")

def lambda_handler():
    dynamodb.