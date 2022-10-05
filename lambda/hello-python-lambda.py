import json

def lambda_handler(event, context):
    nombre = json.loads(event['body'])['nombre']
    if (nombre):
        message = "Hola '" + nombre + "' desde Python!"
    else:
        message = "Hola desde Python!" 
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }