def lambda_handler(event, context):
    api = TodoAPI()
    return {
        "statusCode": 200,
        "body": api.get_list()
    }