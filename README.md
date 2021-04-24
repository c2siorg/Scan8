Scan8
=============
Scan8 is a Kubernetes based rapid URL/File scan system that allows to submit a list of URLs/files and take out the scan results.

## Description
Scan8 uses ClamAV open-source antivirus project as the scan engine and Google gvisor as the container sandboxing for k8. The overall system is able to create a large number of lightweight ClamAV containers (Pods)  and distribute the scan list on demand and take out the scan result within a short amount of time.

## Workflow
- The **shared storage** is divided into 3 components:  
  - **Scan Results**:  
    All the results for the scans conducted are exported here.  
  - **Job Queues**:  
    The queues for all the scanner nodes.  
  - **Scan List**:  
    The master list that contains all the URLs/files to be scanned.  
- **Master/Distribution script** is responsible for periodically appending jobs to the smallest queue of a scanner node.  
- **Scanner script** pops the front file/URL from the job queue and makes it available for the ClamAV script.  
- **ClamAV script** runs the scan on the required file/URL.  
