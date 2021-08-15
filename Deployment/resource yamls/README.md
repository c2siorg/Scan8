# Resource Yamls

In this directory here are .yaml files which are used in scan8-chart.
Subdirectories contain specific .yaml files.

## deployment

***

In the deployment directory, there are deployment files of Dashboard+Coordinator, Mongo, Redis and Worker.

## hpa

***

In hpa, there are two files

1. hpa.yaml is targetting the worker deployment and monitoring the CPU utilization of that deployment.

2. components.yaml which is used as a metrics server and helps to get the metrics of the deployments.

## pv

***

There are other two files which are PV.yaml and PVC.yaml files which are required to use PV in pods.

## service

***

This repository contains service files for all the deployments.
