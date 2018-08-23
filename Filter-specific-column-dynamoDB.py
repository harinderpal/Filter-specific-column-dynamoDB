import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodbResource = boto3.resource('dynamodb')

def lambda_handler(event, context):
    tableName = 'abc'
    columnName = 'searchname'
    columnValue = 'searchvalue'
    onlyColumns = "Selectcolumn"
    table = dynamodbResource.Table(tableName)
    response = table.scan(
        Select='SPECIFIC_ATTRIBUTES',
        ProjectionExpression=onlyColumns,
        FilterExpression=Attr(columnName).eq(columnValue)
        )
    #print("response of getRecordsByColumn",response)
    print(response['Items'])  
