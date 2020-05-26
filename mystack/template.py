from troposphere import Template
import troposphere.ec2 as ec2
t = Template()
instance = ec2.Instance("myinstance")
instance.ImageId = "ami-951945d0"
instance.InstanceType = "t1.micro"
t.add_resource(instance)
print(t.to_json())