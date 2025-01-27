( I accidentially deleted the last page here (cry emoji)... I will rewrite this README using our final deliverable from last semester... must readd how to run from RasPi5 )

SETUP:
* git clone this project
* ensure python is downloaded
* ensure flask is downloaded (python -m pip install flask)
* ensure openvs is downloaded (python -m pip install opencv-python-headless)
  
To use application:

1. In the RCFLASK dir, run 'python3 app.py' or 'python app.py'

2. Click on website

[To edit application, use VS Code, preferably.]

Current Display:

![Current Page](./static/images/concurrentpage.png)

![Current Page 2](./static/images/currentpage2.png)

BlueSky Design:

![Controller Page](./static/images/mainpage.png)

To set Location Permissions, go to the directory and in the terminal run:

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

Then enter: US Florida Gainesville - - 127.0.0.1 -