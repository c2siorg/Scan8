# Scan8
Scan8 is a Kubernetes based rapid URL/File scan system that allows to submit a list of URLs/files and take out the scan results.  Scan8 uses ClamAV open-source antivirus project as the scan engine and Google gvisor as the container sandboxing for k8. The overall system is able to create a large number of lightweight ClamAV containers (Pods)  and distributed the scan list on demand and take out the scan result within a short amount of time.
![scan8](https://user-images.githubusercontent.com/20130001/119669658-d893e200-be55-11eb-8eeb-4d698e0cfe7c.png)

## Dependencies:
* Language: ```Python 3.8.10```
* Database: ```MongoDB```
* redis-server

> Specific dependencies for the ```Dashboard```, ```Coordinator``` and ```Worker``` can be found in the respective directories in ```requirements.txt``` file.

## Local setup guide
1. Clone the current repository to your local machine using ```git clone```.
2. Install the dependencies as specified in ```Dependencies``` section.
3. Make sure the ```mongod``` service is running in the background and check the ```.env``` file to have the appropriate MongoDB host and port (variables are set to defaults).
4. Access the terminal and move to the ```Dashboard``` directory.
5. Run the flask application using ```export FLASK_APP=app.py``` followed by ```flask run```.
6. Access another terminal and move to the ```Coordinator``` directory.
7. Run the coordinator node application using ```python3 app.py```.
8. Access another terminal and move to the ```Worker``` directory.
9. Run the worker node application using ```python3 app.py```.
10. Create ```Uploads``` and ```Results``` directories in the project directory.

## Usage
1. After following the ```Local setup guide```, use any web browser to access the IP address mentioned in the terminal after running ```flask run``` (by default it is ```http://127.0.0.1:5000/```).
2. Submit new scans using the ```New Scan``` button and track their progress on the dashboard.
3. The results for the submitted scans can be found in the ```Results``` directory as ```<scan id>_<file_name>.json```.
