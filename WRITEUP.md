
# Microsoft Azure Writeup

## Deploy an Article CMS to Azure

### App Service:
>Azure Web Apps is a fast and simple way to create web apps using ASP.NET, Java, Node.js or PHP.It has built-in CI/CD integration and has zero-downtime deployments. Its take away most of the complexity and lets us concentrate more on the application itself.

Approx Monthly cost:

| Service | Cost (Per Month)|
| ------ | ------ |
| App Service | $55 |
|Storage account | $22 |
|SQL Database cost | $373 |
#### Approximate Total $450

### Pros:
- It has built in infrastructure maintenance, scaling.
- high availability with SLA-backed uptime of 99.95 %
- Continuous Deployment (CI / CD) workflow backed up with [AzureRepos, GitHub, BitBucket]

### Cons:
- Provides no control over the infrastructure 

### Virtual Machines:
>Azure Virtual Machines let us provision Windows or Linux VMs in seconds, can be deployed with own VM image or images from the Azure Marketplace, ability to scale from one to thousands of VM instances in minutes with Azure Virtual Machine Scale Sets.

Approximate Monthly cost:

| Service | Cost (Per Month)|
| ------ | ------ |
| Virtual Machine | $153 |
|Storage account | $22|
|SQL Database cost | $373 |
#### Approximate Total $548

### Pros:
- It provides complete control over infrastructure.
- high availability with SLA-backed uptime of 99.5%
- can be scaled from one to thousands of VM instances.
- 
### Cons:
- Increased Complexity compared to App Service

## Summary
>As the application is a not business critical and it requires much less managerial efforts, I used App Service.
In future I might add more functionality to the app and we might require better control over the deployment or decide to write business critical articles or ultimate usage of the app might increase.
>In that case I would migrate to Virtual Machines and use Higher Tier SQL database for better access and security. New Plan will be according to the budget threshold.

