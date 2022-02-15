Scan8 (Open for GSoC 22)
========

Scan8 is a distributed scanning system for detecting trojans, viruses, malware, and other malicious threats embedded in files. The system will allow one to submit a list of URLs or files and get the scan results in return.  

The project is divided into various modules namely ```Dashboard```, ```Coordinator Node```, ```Worker Node```, and ```Testing```.  
The ```Dashboard``` provides a responsive web interface for uploading files for new scans and tracking the status of all the submitted scans.  
The ```Coordinator Node``` listens to updates for new scans, subsequently creating and adding scan jobs to the Redis Queue.  
The ```Worker Node``` listens to updates for new jobs in Redis Queue and executes them.  
The ```Testing``` module helps in maintaining the application and facilitating the CI/CD process for the same.

## Application Architecture
![Scan8 application architecture](https://user-images.githubusercontent.com/54113320/129327795-bd8da18e-484a-428a-aa90-7cc063e11b7f.png)

## Dependencies
* Language: ```Python 3.8.10```
* Database: ```MongoDB```
* Tools: ```redis-server clamav clamav-daemon```

> Specific dependencies for the ```Dashboard```, ```Coordinator``` and ```Worker``` can be found in the respective directories in ```requirements.txt``` file.


## Local Setup Guide
1. Clone the current repository to your local machine using ```git clone```.
2. Install the dependencies as specified in ```Dependencies``` section.
3. Make sure the ```mongod``` and ```clamav-daemon``` services are running in the background.
4. Check the ```.env``` file to have the appropriate MongoDB and Redis host and port (variables are set to defaults).
5. Access the terminal and move to the ```Dashboard``` directory.
6. Run the flask application using ```export FLASK_APP=app.py``` followed by ```flask run```.
7. Access another terminal and move to the ```Coordinator``` directory.
8. Run the coordinator node application using ```python3 app.py```.
9. Access another terminal and move to the ```Worker``` directory.
10. Run the worker node application using ```python3 app.py```.
11. Create ```Uploads``` and ```Results``` directories in the project directory.


## Usage
1. After following the ```Local setup guide```, use any web browser to access the IP address mentioned in the terminal after running ```flask run``` (by default it is ```http://127.0.0.1:5000/```).
2. Submit new scans using the ```New Scan``` button and track their progress on the dashboard.
3. The results for the submitted scans can be found in the ```Results``` directory as ```<scan id>_<file_name>.json```.

## Testing
The application comes with a test suite to help users ensure correct installation and help developers verify any updates.
1. Ensure the Results and Uploads directories are empty.
2. Ensure the MongoDB collections are empty.
3. Ensure the scan8 application is up and running.
4. Access a terminal and move to the ```Testing``` directory.
5. Run the test suite using ```python3 app.py -v```.
7. Run a single scan using the Scan8 dashboard and wait till completion.
8. Run the test suite again using ```python3 app.py -v```.

## Demo videos
* [Introduction](https://drive.google.com/file/d/16oXRxPhDIK1QnPnjoJig_SXpZj8Lj-mq/view?usp=sharing)
* [Application Demo](https://drive.google.com/file/d/1TblQdpIAS4VybZzgb2ORfmJiXs_McVrO/view?usp=sharing)
* [Testing Demo](https://drive.google.com/file/d/1CTvLrD_fSdq6xxXabgkLGOPs3jDLwPrT/view?usp=sharing)
