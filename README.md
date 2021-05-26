# Scan8
Scan8 is a Kubernetes based rapid URL/File scan system that allows to submit a list of URLs/files and take out the scan results.  Scan8 uses ClamAV open-source antivirus project as the scan engine and Google gvisor as the container sandboxing for k8. The overall system is able to create a large number of lightweight ClamAV containers (Pods)  and distributed the scan list on demand and take out the scan result within a short amount of time.
![scan8](https://user-images.githubusercontent.com/20130001/119669658-d893e200-be55-11eb-8eeb-4d698e0cfe7c.png)

