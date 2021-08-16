# Helm Chart

This helm chart implementation is an umbrella chart implementation in which there is one main chart and other charts are inside it.
The main chart is scan8-chart inside which there are multiple charts which are dashboard_coordinator, database, worker charts.

## dashboard_coordinator

In dashboard_coordinator there are 4 files which are dashboard+coordinator.yaml is a deployment file for the dashboard and dashboard-service which is a service file for the dashboard deployment.
There are other two files which are PV.yaml and PVC.yaml files which are required to use PV in pods.

## database

In the database chart, there are two deployments files which are of Redis and MongoDB and their respective service files.

## worker

In the worker chart, there are two files which are a worker.yaml(Deployment) and hpa.yaml(HPA for the worker).

## Dependencies

***

* Helm charts installed and configured.

## Usage

***

1. cd into the Scan8/Deployment/charts.

2. helm install "chart name you want to give" scan8-chart.

3. Use any web browser to access the IP address (by default it is http://127.0.0.1:30110/).