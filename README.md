# meetupv6
AWS SDK for Python (Boto3)

AWS credential setting
-----------
First, install the library and set a default region:

.. code-block:: sh

    $ pip install -r requirements.txt

Next, set up credentials (in e.g. ``~/.aws/credentials``):

.. code-block:: ini

    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET

Then, set up a default region (in e.g. ``~/.aws/config``):

.. code-block:: ini

    [default]
    region=us-east-1
    

Demo included scripts for:
   - SNS notification via mail
     Required topic_arn ex: arn:aws:sns:ap-northeast-1:5...
     
   - S3
     Required bucket_name
     
   - EC2
     Required [ImageId], [KeyPairName], [SecurityGroupIds] 
