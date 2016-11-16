import pprint

import boto3

ec2 = boto3.resource('ec2')
#ec2_client = boto3.client('ec2')
pp = pprint.PrettyPrinter(indent=2)

def config_cloud_init():
    """
    Running Commands on Your Linux Instance at Launch
    http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
    """

    return """
        #cloud-config
        repo_update: true
        repo_upgrade: all

        packages:
         - httpd24

        runcmd:
         - service httpd start
         - chkconfig httpd on
    """

def create_ec2_instance():
    cloud_config = config_cloud_init()
    instance = ec2.create_instances(
        DryRun=False,
        ImageId= 'your_ami_id',
        MinCount=1,
        MaxCount=1,
        KeyName='your_key_pair',
        SecurityGroupIds=['your_security_group'],
        UserData=cloud_config,
        InstanceType='t2.nano',
        InstanceInitiatedShutdownBehavior='stop'
    )
    pp.pprint(instance)
    print('Instance was created!')


def run():
    #send_notification()
    create_ec2_instance()

if __name__ == '__main__':
    run()
