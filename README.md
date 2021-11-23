
## Task 1
 Task one contains 2 script file written in bash. These scripts are to automate the installation process of docker. This script pulls and installs the latest version of of docker. If it find the docker is already installed and its version if it is old then this script will remove the the older version of docker and will install the latest version of docker. After installing the docker successfully the script will pull `Elasticsearch` and Kibana `Docker` image. 

**Run Script:**
1. Keep both script on the same folder
2. Navigate to the folder with `cd task_1`
3. Give the script executable permission `chmod +x docker_install.sh docker_install_process.sh`
4. Inside the folder run the script: `Sudo ./docker_install.sh`

**Verify:**
Open a new terminal and put `sudo docker pa -a` . if it run properly the everything is working fine

## Task 2

This task contain a single script which run `Elasticsearch` on **port:2048** and `Kibana` on **port:4096**
**Run Script:**

1. Navigate to the folder of task_2  `cd task_2`
2. Give the script executable permission by `chmod +x run_elasticSearch_and_kibana.sh`
3. Run the script by `sudo ./run_elasticSearch_and_kibana.sh`
4. Wait for a while to gets things ready 
5. Navigate to browser [http://localhost:4096](http://localhost:4096)

**Verify:**
http://localhost:4096 address will navigate to the Dashboard

## Task 3
In this task, python scripts will push data to our previously running Elasticsearch. That script will push 10 student data within five-minute boundaries.
**Run Script:**
1. Navigate to the python folder `cd task_3`
2. Activate the Python environment: `source my-env/bin/activate`
3. Simply run the `python run_schedular.py`

**Verify:**
Student data will be shown on the Terminal


# Thanks