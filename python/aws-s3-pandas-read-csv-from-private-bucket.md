## Problem
AWS and Pandas: reading a CSV object from a private S3 bucket
* `pandas.read_csv()` can read directly from a public URL like `pd.read_csv('s3://path/to/table.csv')`
* this does not work for a private S3 bucket

## Solution
* use boto3 to get a response from the S3 service client
* the 'Body' key contains a StreamingBody/file-like object that you can now pass to `pd.read_csv()`
* supply your own `.env` file, `bucket_name`, and `object_key` to reproduce the example

```python
import os

import boto3
import dotenv
import pandas as pd

# load from .env file and over-ride any existing variables
dotenv.load_dotenv('../.env', override=True)

bucket_name = ''
object_key = ''

# start s3 service
s3_client = boto3.client('s3',
                         aws_access_key_id=os.environ['ACCESS_KEY'],
                         aws_secret_access_key=os.environ['SECRET_KEY'],
                         region_name=os.environ['REGION_NAME'],
                         )

response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
file_obj = response['Body']

df = pd.read_csv(file_obj)
```
