Expand date spans to year-month view

```sas
data test;
input client $ pmpm start_yrmo end_yrmo;
datalines;
client1 234.56 201801 201803
client2 300.00 201811 201902
;
run;

%macro expand_data(indata=,outdata=);
     data &outdata.;
           set &indata.;
                do i = start_yrmo to end_yrmo;
                  if i=start_yrmo then j=0;
                 j=j+1;
                  if mod(i,100)=13 then i=i+88;
                 output;
                end;
     run;
%mend expand_data;

%expand_data(indata=test,outdata=test2);
```

___

test
|    | client   |   pmpm |   start_yrmo |   end_yrmo |
|---:|:---------|-------:|-------------:|-----------:|
|  0 | client1  | 234.56 |       201801 |     201803 |
|  1 | client2  | 300    |       201811 |     201902 |

test2
|    | client   |   pmpm |   start_yrmo |   end_yrmo |      i |   j |
|---:|:---------|-------:|-------------:|-----------:|-------:|----:|
|  0 | client1  | 234.56 |       201801 |     201803 | 201801 |   1 |
|  1 | client1  | 234.56 |       201801 |     201803 | 201802 |   2 |
|  2 | client1  | 234.56 |       201801 |     201803 | 201803 |   3 |
|  3 | client2  | 300    |       201811 |     201902 | 201811 |   1 |
|  4 | client2  | 300    |       201811 |     201902 | 201812 |   2 |
|  5 | client2  | 300    |       201811 |     201902 | 201901 |   3 |
|  6 | client2  | 300    |       201811 |     201902 | 201902 |   4 |
