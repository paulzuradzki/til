How to connect to AWS S3 and post objects.

For more, see:
https://realpython.com/python-boto3-aws-s3/

```python
"""aws_dev.py

AWS S3 is a block file storage service.
* The "block-object" model is somewhat analagous to the file-directory mental model that we commonly use for a file system.
* S3 is like renting cheap storage for large datasets whereas EC2 is like renting a full computer.
    * Analogy: you might buy an external SSD to store large video files rather than using up your PC's hard disk storage. 
    * This lets you keep your PC storage modest.
    * S3 buckets have additional functionality such as portability, where they can be access from other machines.
    * This is analogous to how an external SSD is portable across computers too.
"""
import boto3      # python -m pip install boto3

# connect to AWS S3
s3_resource = boto3.resource('s3',
                             aws_access_key_id='YOUR_KEY',
                             aws_secret_access_key='YOUR_KEY'
                             )

# make a file
with open('hello.txt', 'w') as f:
    f.write('hello, world')

# upload file to a bucket
s3_resource.Object('test-bucket-9725', 'hello.txt').upload_file(Filename='hello.txt')

# list buckets
for bucket in s3_resource.buckets.all():
    print(bucket.name)                             # => test-bucket-9725

# list objects inside a bucket
bucket = s3_resource.Bucket('test-bucket-9725')
for obj in bucket.objects.all():
    print(obj.key)                                 # => hello.txt

```