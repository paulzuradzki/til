Loops in SAS 🤮
```sas

/*data set to loop through*/

data t;
input city $ state $ full & : $100.;
datalines;
Chicago Illinois Chicago, IL
Bloomington Indiana Bloomington, IN
Arlington Virginia Arlington, VA
;
run;

/****************************************************************/
/*METHOD 1 - _null_ data step with symputx*/
/****************************************************************/

/* create variables for each record in the table
/*SYNTAX: CALL SYMPUT(MacroVariable, Value);*/
data _null_;
	set work.t end=no_more;
	call symputx('city'||left(_n_),city);
	call symputx('full'||left(_n_),full);
	if no_more then call symputx('numrows',_n_);
run;

/*putLoop for debugging*/
	/*alternatively, use %sysfunc(countw(&list.)) to find the length of the list*/
	/*%do i = 1 %to %sysfunc(countw(&list.));*/
%macro putloop;
%do i = 1 %to &numrows;
	%put item &i. is &&full&i.;
%end;
%mend putloop;
%putloop


/****************************************************************/
/*METHOD 2 - procsql array macro variables*/
/****************************************************************/

PROC SQL noprint;
SELECT count(*)
INTO :numrows
FROM WORK.t
;
quit;
%put numrows is: &numrows;

/* create macro array variables for each record in the table
cpath1, cpath2, cpath3, etc. */
PROC SQL noprint;
SELECT 
	city,
	full
INTO
	:city-,    /* same as  :city1-cityN,*/
	:full-      /* same as  :full1-fullN*/
FROM WORK.t
;
quit;
%putloop

/****************************************************************/
/*METHOD 3a - scanning through delimited string (ex: space delimiter)*/
/****************************************************************/
%let list = Chicago Bloomington Arlington;

/* COUNTW counts # of words in a character string */
/* SCAN returns the n-th word in a string
	syntax: scan(string, n, delimiter) */

/*putLoop for debugging*/
%macro putloop;
%do i = 1 %to %sysfunc(countw(&list.));
	%let item = %scan(&list, %eval(&i), " ");
	%put item on iteration &i. is &item;
%end;
%mend;
%putloop

/****************************************************************/
/*METHOD 3b - create space-delimeted list through proc sql array*/
/****************************************************************/

/*create a space-separated list*/
PROC SQL noprint;
SELECT 
	city,
	state
INTO 
	:city_list separated by ' ',
	:state_list separated by ' '
FROM WORK.t
;
quit;

/* COUNTW counts # of words in a character string */
/* SCAN returns the n-th word in a string
	syntax: scan(string, n, delimiter) */

/*putLoop for debugging*/
%macro putloop;
%do i = 1 %to %sysfunc(countw(&city_list.));
	%let city = %scan(&city_list, %eval(&i), " ");
	%put city on iteration &i. is &city;

	%let state = %scan(&state_list, %eval(&i), " ");
	%put state on iteration &i. is &state;

%end;
%mend putloop;
%putloop
```

___

Data set to loop through
|    | city     | state    | full            |
|---:|:---------|:---------|:----------------|
|  0 | Chicago  | Illinois | Chicago, IL     |
|  1 | Blooming | Indiana  | Bloomington, IN |
|  2 | Arlingto | Virginia | Arlington, VA   |

___

SAS Log
```
1                                                          The SAS System                                12:34 Tuesday, May 19, 2020

1          ;*';*";*/;quit;run;
2          OPTIONS PAGENO=MIN;
3          %LET _CLIENTTASKLABEL='Program (2)';
4          %LET _CLIENTPROCESSFLOWNAME='Process Flow';
5          %LET _CLIENTPROJECTPATH='';
6          %LET _CLIENTPROJECTPATHHOST='';
7          %LET _CLIENTPROJECTNAME='';
8          %LET _SASPROGRAMFILE='';
9          %LET _SASPROGRAMFILEHOST='';
10         
11         ODS _ALL_ CLOSE;
12         OPTIONS DEV=PNG;
13         GOPTIONS XPIXELS=0 YPIXELS=0;
14         FILENAME EGSR TEMP;
15         ODS tagsets.sasreport13(ID=EGSR) FILE=EGSR
16             STYLE=HtmlBlue
17             STYLESHEET=(URL="file:///C:/Program%20Files/SASHome2/SASEnterpriseGuide/7.1/Styles/HtmlBlue.css")
18             NOGTITLE
19             NOGFOOTNOTE
20             GPATH=&sasworklocation
21             ENCODING=UTF8
22             options(rolap="on")
23         ;
NOTE: Writing TAGSETS.SASREPORT13(EGSR) Body file: EGSR
24         
25         GOPTIONS ACCESSIBLE;
26         /*data set to loop through*/
27         
28         data t;
29         input city $ state $ full & : $100.;
30         datalines;

NOTE: The data set WORK.T has 3 observations and 3 variables.
NOTE: DATA statement used (Total process time):
      real time           0.00 seconds
      cpu time            0.00 seconds
      
34         ;

35         run;
36         
37         /****************************************************************/
38         /*METHOD 1 - _null_ data step with symputx*/
39         /****************************************************************/
40         
41         /* create variables for each record in the table
42         /*SYNTAX: CALL SYMPUT(MacroVariable, Value);*/
43         data _null_;
44         	set work.t end=no_more;
45         	call symputx('city'||left(_n_),city);
46         	call symputx('full'||left(_n_),full);
47         	if no_more then call symputx('numrows',_n_);
48         run;

NOTE: Numeric values have been converted to character values at the places given by: (Line):(Column).
      45:28   46:28   
NOTE: There were 3 observations read from the data set WORK.T.
NOTE: DATA statement used (Total process time):
2                                                          The SAS System                                12:34 Tuesday, May 19, 2020

      real time           0.00 seconds
      cpu time            0.00 seconds
      

49         
50         /*putLoop for debugging*/
51         	/*alternatively, use %sysfunc(countw(&list.)) to find the length of the list*/
52         	/*%do i = 1 %to %sysfunc(countw(&list.));*/
53         %macro putloop;
54         %do i = 1 %to &numrows;
55         	%put item &i. is &&full&i.;
56         %end;
57         %mend putloop;
58         %putloop
item 1 is Chicago, IL
item 2 is Bloomington, IN
item 3 is Arlington, VA
59         
60         
61         /****************************************************************/
62         /*METHOD 2 - procsql array macro variables*/
63         /****************************************************************/
64         
65         PROC SQL noprint;
66         SELECT count(*)
67         INTO :numrows
68         FROM WORK.t
69         ;
70         quit;
NOTE: PROCEDURE SQL used (Total process time):
      real time           0.00 seconds
      cpu time            0.00 seconds
      

71         %put numrows is: &numrows;
numrows is:        3
72         
73         /* create macro array variables for each record in the table
74         cpath1, cpath2, cpath3, etc. */
75         PROC SQL noprint;
76         SELECT
77         	city,
78         	full
79         INTO
80         	:city-,    /* same as  :city1-cityN,*/
81         	:full-      /* same as  :full1-fullN*/
82         FROM WORK.t
83         ;
WARNING: INTO Clause :city through : does not specify a valid sequence of macro variables.
WARNING: INTO Clause :full through : does not specify a valid sequence of macro variables.
84         quit;
NOTE: PROCEDURE SQL used (Total process time):
      real time           0.00 seconds
      cpu time            0.01 seconds
      

85         %putloop
item 1 is Chicago, IL
3                                                          The SAS System                                12:34 Tuesday, May 19, 2020

item 2 is Bloomington, IN
item 3 is Arlington, VA
86         
87         /****************************************************************/
88         /*METHOD 3a - scanning through delimited string (ex: space delimiter)*/
89         /****************************************************************/
90         %let list = Chicago Bloomington Arlington;
91         
92         /* COUNTW counts # of words in a character string */
93         /* SCAN returns the n-th word in a string
94         	syntax: scan(string, n, delimiter) */
95         
96         /*putLoop for debugging*/
97         %macro putloop;
98         %do i = 1 %to %sysfunc(countw(&list.));
99         	%let item = %scan(&list, %eval(&i), " ");
100        	%put item on iteration &i. is &item;
101        %end;
102        %mend;
103        %putloop
item on iteration 1 is Chicago
item on iteration 2 is Bloomington
item on iteration 3 is Arlington
104        
105        /****************************************************************/
106        /*METHOD 3b - create space-delimeted list through proc sql array*/
107        /****************************************************************/
108        
109        /*create a space-separated list*/
110        PROC SQL noprint;
111        SELECT
112        	city,
113        	state
114        INTO
115        	:city_list separated by ' ',
116        	:state_list separated by ' '
117        FROM WORK.t
118        ;
119        quit;
NOTE: PROCEDURE SQL used (Total process time):
      real time           0.00 seconds
      cpu time            0.01 seconds
      

120        
121        /* COUNTW counts # of words in a character string */
122        /* SCAN returns the n-th word in a string
123        	syntax: scan(string, n, delimiter) */
124        
125        /*putLoop for debugging*/
126        %macro putloop;
127        %do i = 1 %to %sysfunc(countw(&city_list.));
128        	%let city = %scan(&city_list, %eval(&i), " ");
129        	%put city on iteration &i. is &city;
130        
131        	%let state = %scan(&state_list, %eval(&i), " ");
132        	%put state on iteration &i. is &state;
133        
4                                                          The SAS System                                12:34 Tuesday, May 19, 2020

134        %end;
135        %mend putloop;
136        %putloop
city on iteration 1 is Chicago
state on iteration 1 is Illinois
city on iteration 2 is Blooming
state on iteration 2 is Indiana
city on iteration 3 is Arlingto
state on iteration 3 is Virginia
137        
138        GOPTIONS NOACCESSIBLE;
139        %LET _CLIENTTASKLABEL=;
140        %LET _CLIENTPROCESSFLOWNAME=;
141        %LET _CLIENTPROJECTPATH=;
142        %LET _CLIENTPROJECTPATHHOST=;
143        %LET _CLIENTPROJECTNAME=;
144        %LET _SASPROGRAMFILE=;
145        %LET _SASPROGRAMFILEHOST=;
146        
147        ;*';*";*/;quit;run;
148        ODS _ALL_ CLOSE;
149        
150        
151        QUIT; RUN;
152        
```
