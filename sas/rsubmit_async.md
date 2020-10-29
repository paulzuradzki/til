### Very simple demo of processing two SAS tasks in parallel with RSUBMIT
* Here we call a sleep function twice
* TODO: explore lock statements so certain tasks only start once a dependency has completed

```sas
/*
Two tasks will each sleep for 2 minutes. 
	* Synchronous processing would result in 4 minute duration.
	* Asynchronous should result in 2 minutes plus the overhead of separate task execution and remote logins.
*/

%put START TIME %sysfunc(time(),time8.0);

/* Start parallel processing */
%let rc=%sysfunc(grdsvc_enable(_all_,server=SASApp;jobopts=hrqueue;));
%let hrqueue=queue=normal;

signon task1;
rsubmit task1 wait=no;
data __null__;
call sleep(120, 1);
run;
endrsubmit;

signon task2;
rsubmit task2 wait=no;
data __null__;
call sleep(120, 1);
run;
endrsubmit;

waitfor _all_ task1 task2;
signoff _all_;

%put END TIME %sysfunc(time(),time8.0);

```
