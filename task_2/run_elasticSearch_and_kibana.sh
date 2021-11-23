#!/bin/bash

docker network create elastic
docker run -d --name es01-test --net elastic -p 2048:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.0
docker run -d --network=elastic --name kib1 -p 4096:5601 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.12.0

