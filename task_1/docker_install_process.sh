#!/bin/bash

function install_docker(){
	apt-get update
	echo "updating......"
	apt-get install \
	    ca-certificates \
	    curl \
	    gnupg \
	    lsb-release
#	echo "-------------------------------------------------"
	 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

	echo \
	  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
	  $(lsb_release -cs) stable nightly" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

#	apt-get update

	apt-get install docker-ce
	apt-get install docker-ce-cli
	apt-get install containerd.io
	
	
}




