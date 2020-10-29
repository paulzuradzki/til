### Very simple demo of processing two SAS tasks in parallel with RSUBMIT
* Here we call a sleep function twice
* TODO: explore lock statements so certain tasks only start once a dependency has completed

```sas
/* Start parallel processing */
%let rc=%sysfunc(grdsvc_enable(_all_,server=SASApp;jobopts=hrqueue;));
%let hrqueue=queue=normal;

signon task1;
rsubmit task1 wait=no;
data __null__;
call sleep(30, 1);
run;
endrsubmit;

signon task2;
rsubmit task2 wait=no;
data __null__;
call sleep(30, 1);
run;
endrsubmit;

waitfor _all_ task1 task2;
signoff _all_;

```
