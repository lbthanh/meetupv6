import pprint
import boto3

sns = boto3.client('sns')
pp = pprint.PrettyPrinter(indent=2)


def send_notification():
    topic_arn = u'replace_your_arn'
    message = u'Boto3 Python SDK!'
    subject = '[Devnext:Alert] Script Testing from Python'

    param = {
        'TopicArn' : topic_arn,
        'Message' : message,
        'Subject' : subject
    }
    response = sns.publish(**param)
    pp.pprint(response)
    print('Message has transfered!')

def run():
    send_notification()

if __name__ == '__main__':
    run()
