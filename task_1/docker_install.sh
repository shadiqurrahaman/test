#!/bin/bash

#Check if Docker is installed or not
apt-get update
if [ -x "$(command -v docker)" ]; then
    version_number = "upgradable"
    docker_latest_version="$(apt list docker-ce)"
    if [[ $docker_latest_version == *"upgradable"* ]];then
        echo "Removing Docker"
        apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli
        echo "installing Docker"
        source docker_install_process.sh 
        calling docker install process
        install_docker
        
    else
    
        echo "Docker version is up to date"
    fi
    
else
    echo "installing Docker"
    source docker_install_process.sh 
    install_docker
fi

#pulling ElasticSearch and Kibana
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.12.0
docker pull docker.elastic.co/kibana/kibana:7.12.0


