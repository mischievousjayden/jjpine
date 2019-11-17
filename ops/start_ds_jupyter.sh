#!/bin/bash

sudo docker rm -f jupyter
sudo docker run -it -d --name jupyter -p 8888:8888 -v /jupyter:/home/jovyan/work jupyter/datascience-notebook:latest
