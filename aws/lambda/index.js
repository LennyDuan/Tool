require('babel-polyfill')
const AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient({region: 'eu-west-1'});
const security = process.env.SECURITY;

// List items in a table
export
const list = async (payload, context, callback) => {
  console.log(JSON.stringify(payload));
  const event_security = payload.queryStringParameters.security;
  const event_table_name = payload.queryStringParameters.table_name;
  const scanningParameters = {
    TableName: event_table_name,
  }
  try {
    const data = await docClient.scan(scanningParameters).promise();
    callback(null, data)
  } catch(error) {
    console.log(error);
    callback(error, 'Unable to scan this table')
  }
};
