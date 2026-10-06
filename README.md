\# Healthcare Vital Signs Monitoring Dashboard



A beginner-level cloud deployment project developed as part of my SIWES training. The project demonstrates the development and deployment of a Django-based healthcare vital signs monitoring dashboard using Docker and Amazon Web Services (AWS).



\## Project Overview



The application provides a simple dashboard for recording and viewing simulated patient vital signs. It was developed to demonstrate practical knowledge of Python, Django, Linux, containerization, networking, and cloud infrastructure.



The application records:



\- Patient ID

\- Patient name

\- Temperature

\- Heart rate

\- SpO₂

\- Blood pressure

\- Recorded time



The project uses simulated data and is intended for educational purposes only. It is not a clinical or diagnostic system.



\## Technologies Used



\- Python

\- Django

\- Git and GitHub

\- Linux

\- Docker

\- Docker Hub

\- Amazon EC2

\- Amazon VPC

\- Internet Gateway

\- NAT Gateway

\- Amazon S3



\## AWS Architecture



The application was deployed using a basic AWS network architecture consisting of:



\- One VPC

\- One public subnet

\- One private subnet

\- One Internet Gateway

\- One NAT Gateway

\- One public EC2 instance serving as a bastion/jump server

\- One private EC2 instance hosting the Django application

\- Security groups controlling network access

\- Amazon S3 for object storage



The private EC2 instance does not have a public IP address. Access to the deployed application was tested through an SSH tunnel via the public EC2 instance.



\## Docker Deployment



The Django application was containerized using Docker and the resulting image was published to Docker Hub.



Docker Hub image:



`maryamqg1/healthcare-vital-monitor:latest`



The private EC2 instance pulls the image and runs the Django application inside a Docker container.



\## Amazon S3



An S3 bucket was created to demonstrate cloud object storage. A project information text file was uploaded as an object.



\## Project Status



The application was successfully deployed and tested on a private EC2 instance. The dashboard, data entry, and readings/history functions were tested through the browser.



\## Educational Purpose



This project was completed as a practical demonstration of foundational knowledge gained during SIWES training in Python programming, cloud computing, Linux server administration, and containerization.

