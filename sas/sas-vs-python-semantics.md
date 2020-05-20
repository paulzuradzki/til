Comparing terminology for similar concepts in Python and SAS

```sas
/*	SAS vs. Python semantics
	* Macro variables -> like Python variables
	* Macro programs -> like user-defined Python functions
	* Macro functions -> existing SAS functions; like Python functions;
						e.g., %sysfunc(), %scan(), etc.
*/

%macro hello(string);   /* arguments */
	%put string is: %upcase(&string.);
%mend;

%put ************;
%hello(HelloWorld); /* "function" call */

%let other_string = HelloAgain;
%hello(&other_string.);

/*
	%hello() is a macro program that takes a string as an argument
	&string. is a macro variable created while calling the macro %hello(); 
		"string" is the argument
	&other_string. is a macro variable created through a %let statement 
	%upcase is a macro function
*/

/*
==============
PUT RESULTS
==============
	40         %hello(HelloWorld);
	string is: HELLOWORLD
	41         
	42         %let other_string = HelloAgain;
	43         %hello(&other_string.);
	string is: HELLOAGAIN
*/
```
