# Monitor Application

Hey there!

I will walk you through this project so you can understand how to run this **Django** website. Let's get started!

 - Clone this repository.
 - Install docker, docker-compose **DIY**.
 - Go to the project root directory.
 - Run `docker-compose up -d`.
 - After the building process open http://127.0.0.1:800/ you will see this home page.
	![alt text](https://github.com/s-azaar/monitor-app/blob/ec0d7e7ea31fc4ed81d93bd23ab540ef78e94bef/img/home.png)
 - And if you tried to access any of the below buttons you will not see anything there, cuz we didn't start the **cron** job to start collecting the server's usages.
 - So get your hands dirty and make sure to do the following things in order: 
	 - Make sure you downloaded the **cron** software.
	 - open crontab file by using this command `crontab -e`.
	 - Type in the opened file this command:
		- `*/1 * * * * /path/to/executable/python /path/to/collector.py`.
		- P.S. File collector.py you can find it in the project root directory. 
		- P.S. This job will run every min just for testing.
	- Activate the **cron** software by using `service cron start`.
 - Now return back to the home page and navigate between the buttons to view the magic.
 - Images:
 - ![alt text](https://github.com/s-azaar/monitor-app/blob/ec0d7e7ea31fc4ed81d93bd23ab540ef78e94bef/img/CPU.png)
 - ![alt text](https://github.com/s-azaar/monitor-app/blob/ec0d7e7ea31fc4ed81d93bd23ab540ef78e94bef/img/Disk.png)
 - ![alt text](https://github.com/s-azaar/monitor-app/blob/ec0d7e7ea31fc4ed81d93bd23ab540ef78e94bef/img/Memory.png)



 - You can find my image on docker hub, kindly use this command `docker pull sazaar/frepo:v1`
