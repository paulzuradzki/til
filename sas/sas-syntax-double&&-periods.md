Disambiguating double ampersand and period in SAS macro variables

```sas
/************************************************/
/************************************************/

/*USE OF INDIRECT REFERENCES AND AMPERSAND MACRO SYNTAX*/

%LET CLIENT=beep_beep;
%LET N=5;
%LET CLIENT5=doop_doop;

%put & double ampersand resolves as one indirect reference: 
	CLIENT_UNRESOLVED_WORD + N_RESOLVED = &&CLIENT&N.;

%put && single ampersand resolves separately: 
	CLIENT_RESOLVED + N_RESOLVED = &CLIENT&N.;

/************************************************/
/************************************************/

/*PERIODS TO RECOGNIZE END OF REFERENCE*/

/*	Sometimes when you use a macro variable reference as a prefix, 
	the reference does not resolve as you expect if you simply concatenate it. 
	Instead, you might need to delimit the reference by adding a period to the end of it.
	A period immediately following a macro variable reference acts as a delimiter. 
	That is, a period at the end of a reference forces the macro processor 
	to recognize the end of the reference. The period does not appear in the resulting text.
*/

%let name=sales;

/*  first attempt to add suffixes--incorrect  */
data &name1 &name2;
   set in&name.temp;
run;

/*After macro variable resolution, SAS sees these statements:*/
DATA &NAME1 &NAME2;
	   SET INSALESTEMP;
RUN;

/*
	None of the macro variable references have resolved as you intended. 
	Because NAME1 and NAME2 are valid SAS names, 
	the macro processor searches for those macro variables rather than for NAME, 
	and the references pass into the DATA statement without resolution.
*/

/*  correct version  */
data &name.1 &name.2;

/*SAS now sees this statement:*/
DATA SALES1 SALES2;
```
