# Assignment #10

# Cisco DNA Center Network Automation (Assignment 9)

## Description
This project is a Django-based web application that interacts with Cisco DNA Center APIs to automate network tasks.

## Features
- Authentication with Cisco DNA Center
- Retrieve network device inventory
- Fetch interface details for devices
- Store logs in MongoDB

## Technologies Used
- Django
- Python (requests, pymongo)
- MongoDB
- AWS EC2 (Amazon Linux 2023)

## Setup Instructions

1. Install dependencies:
pip install -r requirements.txt

2. Run the server:
python manage.py runserver 0.0.0.0:8000

## Access URLs

- Authentication:
  /auth/

- Devices:
  /devices/

- Interfaces:
  /interfaces/?ip=<device_ip>