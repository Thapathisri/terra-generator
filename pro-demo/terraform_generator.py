# terraform_generator.py
from jinja2 import Environment, FileSystemLoader
import os

# Set up Jinja2 environment
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)

def generate_terraform(template_name, data, output_file):
    # Render template
    template = env.get_template(f'aws/{template_name}.tpl')
    output = template.render(data)

    # Write output to file
    with open(output_file, 'w') as f:
        f.write(output)

    print(f'Terraform file generated: {output_file}')

# Define input data for AWS resources
aws_s3_data = {
    'bucket_name': 'tanni-20',
    'acl': 'private',
    'region': 'ap-south-1'
}

aws_ec2_data = {
    'instance_name': 'my-instance',
    'ami': 'ami-12345678',
    'instance_type': 't2.micro',
    'key_name': 'my-keypair',
    'subnet_id': 'subnet-12345678'
}

aws_vpc_data = {
    'vpc_name': 'my-vpc',
    'cidr_block': '10.0.0.0/16',
    'instance_tenancy': 'default'
}

# Generate Terraform files for AWS resources
generate_terraform('s3_bucket', aws_s3_data, 'generated_aws_s3.tf')
generate_terraform('ec2_instance', aws_ec2_data, 'generated_aws_ec2.tf')
generate_terraform('vpc', aws_vpc_data, 'generated_aws_vpc.tf')
