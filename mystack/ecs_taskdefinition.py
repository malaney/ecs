from troposphere import Join, Template, Ref, AWS_ACCOUNT_ID, AWS_REGION

from troposphere.ecs import (
    ContainerDefinition,
    Environment,
    PortMapping,
    TaskDefinition,
)

template = Template()
app_revision = 'latest'
repository = 'nick'

web_task_definition = TaskDefinition(
    "WebTask",
    template=template,
    Condition='foo',
    ContainerDefinitions=[
        ContainerDefinition(
            Name="WebWorker",
            #  1024 is full CPU
            Cpu=8,
            Memory=2048,
            Essential=True,
            Image=Join("", [
                Ref(AWS_ACCOUNT_ID),
                ".dkr.ecr.",
                Ref(AWS_REGION),
                ".amazonaws.com/",
                Ref(repository),
                ":",
                app_revision,
            ]),
            PortMappings=[PortMapping(
                ContainerPort=10,
                HostPort=8000,
            )],

            Environment=[
                Environment(
                    Name="AWS_STORAGE_BUCKET_NAME",
                    Value='blah',
                ),
                Environment(
                    Name="CDN_DOMAIN_NAME",
                    Value="DomainName"
                )
            ],
        )
    ],
)

print(template.to_yaml())
