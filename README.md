# Scan8
Scan8 is a Kubernetes based rapid URL/File scan system that allows to submit a list of URLs/files and take out the scan results.  Scan8 uses ClamAV open-source antivirus project as the scan engine and Google gvisor as the container sandboxing for k8. The overall system is able to create a large number of lightweight ClamAV containers (Pods)  and distributed the scan list on demand and take out the scan result within a short amount of time.

### Initial System Architecture
![initial_sys_architecture](https://user-images.githubusercontent.com/59219626/110995554-8c7de900-83a0-11eb-8045-d8815fe075f8.png)
