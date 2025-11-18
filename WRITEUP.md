# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

This project involves deploying a simple Article CMS application to Microsoft Azure using App Service and GitHub Actions for automated CI/CD. The CMS is hosted in a fully managed environment where Azure handles updates, runtime management, and scaling. The project includes configuring the necessary Azure resources, connecting the GitHub repository to Azure Deployment Center, and validating the deployment by creating a sample article in the app. It also requires analyzing Azure App Service and Virtual Machine hosting options to select the most appropriate deployment method based on cost, scalability, maintenance, and workflow. Overall, the project demonstrates cloud deployment, automation, and architectural decision-making.

1.AZURE APP SERVICES

Azure App Service is a fully managed "Platform as a Service" (PaaS) for hosting web applications. You just upload your code, and Azure handles all the servers, networking, and operating system updates for you.

Pros:
It's fully managed by Azure (no OS or Nginx setup), deployment is automated via GitHub, secrets are stored securely, and it has a free tier.
Cons:
You lose direct server control (no ssh access) and debugging is limited to logs, which can be more abstract than a live terminal.

2.Azure Virtual Machine

An Azure Virtual Machine (VM) is an "Infrastructure as a Service" (IaaS) that gives you a complete, emulated computer in the cloud. You get full ssh (root) access to the server, but you are responsible for managing everything, including the operating system, security patches, and web server installation.
Pros:
It gives you total root control to ssh in and install any custom OS, software, or networking configuration you need.
cons:
It's extremely complex (you manage all OS patches, Nginx, and security), the workflow is completely manual, and it has no free tier.

Azure App Service is the best choice because it's a PaaS (Platform as a Service), which means Azure fully manages the underlying infrastructure, operating system (Linux), and web server (Nginx/Gunicorn). This avoids the massive complexity and manual setup of a Virtual Machine (IaaS), where we would have been responsible for installing and patching everything ourselves. The workflow is automated via the "Deployment Center," which connects directly to GitHub for seamless CI/CD, and secrets are stored securely in the "Configuration" tab, not in code.For this project, the App Service is more cost-effective (it has a free tier), easier to scale, and allows us to focus 100% on the Python application, not server administration.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

The decision of using Azure App Services can be changed to Azure Virtual machines can be done when use of a Virtual Machine application's needs grew beyond what the App Service platform offers. For example, if this project expanded to require a non-HTTP background service, like a custom-built video processing queue, a VM would be necessary.  A VM would also be the correct choice if the app had a hard dependency on a specific older version of Ubuntu, required `ssh`/root access to install custom system libraries, or needed to be co-located on the same server with other non-Python applications to save costs. These scenarios would justify the added complexity and manual management of a VM over the simplicity of an App Service.

Conclusion:
In conclusion, this project demonstrated the successful deployment of a full-stack Python Flask application to the cloud. By selecting Azure App Service (PaaS) over a Virtual Machine (IaaS), it prioritized a simple, automated workflow and managed security, which proved to be the most efficient choice for this application.The final, deployed application successfully connects to both the Azure SQL Database for post data and Azure Blob Storage for image hosting, fulfilling all project requirements.
