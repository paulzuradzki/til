# Implementing HEDIS continuous enrollment requirements for healthcare quality measures

**Description**
I’ve come across and tried several complicated implementations of the HEDIS continuous enrollment algorithm (SAS, SQL, NumPy, tricky date gap rules). I think using string operations with regular expressions has been the most clear and compact approach for me.

**Background**
* HEDIS quality measures are a standard set of clinical quality measures used to evaluate health plans and identify gaps in care. HEDIS is published and specified by NCQA. There are additional quality rating systems but we will focus on HEDIS. 
* `Continuous enrollment` - Most HEDIS measures have continuous enrollment requirements. Continuous enrollment requirements specify the minimum amount of time that a patient must be enrolled in an organization before becoming eligible for a measure. It ensures that the  organization has enough time to render services.
* `Allowable gaps` - A gap is the time when a patient is not covered by the organization (i.e., the time between disenrollment and re-enrollment). An allowable gap can occur anytime during continuous enrollment. If the organization applied a full-month eligibility criterion to beneficiaries and verifies enrollment prospectively in monthly intervals, the one gap in enrollment during the continuous enrollment period may not exceed 45 days. For example, a member whose coverage lapses for 2 months (60 days) is not considered continuously enrolled.

**Objective**
* Given a sequence of 24 ones and zeroes (e.g., `111001011111111101110001`), we want to return a True or False value for whether the following requirements are met.
    * A one represents a month of enrollment. A zero is a single month gap (30 days). 
    * sequence[0-11] is the calendar year prior to the measurement period. sequence[12-23] is the measurement period.
* *Requirements*
    * The value at index 12 must be 1
        * The member must be enrolled at the start of the measurement period.
    * There is no sequence of 0’s that is greater than length one. 
        * Ex:, “110011” is not allowed because the sequence of zeroes is two-characters long.
        * This rule captures that an allowable gap must be less than 45 days. Two zeroes (two months) would be 60 days which exceeds the allowable threshold.
    * No more than one sequence of zeroes (any length) in the first and second half of the input.
        * One allowable gap (<45 days) per calendar year is allowed.

We will assume that we have data representable as a string or an array of ones and zeroes. We will focus on the algorithm rather than data preparation. E.g., enrollment data may be stored as date spans that require transformation before we have a cleaned up member-month or member-day sequence.

**Example** 
* Sequence: `111001011111111101110001`
* This sequence has 4 gaps (4 sequences of 0's). They are: `['00', '0', '0', '000']`.
* 2 gaps are allowable because they have length of one ('0' has length 1) and only one occurs per calendar year. 
* 2 gaps are not allowable because they have a length exceeding 1 ('00' has length 2, '000' has length 3)
* Since we have more than one non-allowable gap, this sequence would be classified as False or "not continuously enrolled"


```python
import re
from pprint import pprint

def is_continuously_enrolled(sequence, verbose=False):
    """
    Example
    -------
    >>> seq = '111001011111111101110001'
    >>> process_input(seq, verbose=True)
        sequence: 111001011111111101110001
        lenght of period: 24
        gaps: ['00', '0', '0', '000']
        nbr_gaps: 4
        len_gaps: [2, 1, 1, 3]
        gaps_non_allowable: 2
        gaps_allowable: 2
    """
    assert len(sequence)==12 or len(sequence)==24, 'Invalid sequence length'
    # regex: collect any sequence of one or more 0's
    rgx = re.compile(r'0+')
    gaps = rgx.findall(sequence)
    nbr_gaps = len(gaps)

    # get the length of the gaps by counting the zeroes in each gap
    len_gaps = [len(gap) for gap in gaps]

    # gap greater than 45 days
    nbr_non_allowable_gaps = sum([1 for gap_length in len_gaps if gap_length>1])
    has_no_45_plus_day_gaps = nbr_non_allowable_gaps==0
    

    # one allowable gap of 45 days or less is allowed per year
    if len(sequence)==24:
        year1_elig_months = sum(int(i) for i in sequence[:12])
        year2_elig_months = sum(int(i) for i in sequence[12:])
        within_allowable_gaps = year1_elig_months>=11 and year2_elig_months>=11
        
        # check if enrolled at beginning of measurement year
        enrolled_at_measure_year_start = sequence[12]=='1'

    if len(sequence)==12:
        year1_elig_months = sum(int(i) for i in sequence[:12])
        within_allowable_gaps = year1_elig_months>=11
        enrolled_at_measure_year_start = sequence[0]=='1'
        
    continuously_enrolled = within_allowable_gaps and has_no_45_plus_day_gaps and enrolled_at_measure_year_start

    if verbose:
        params = {'sequence': sequence,
                  'length_of_period': len(sequence),
                  'gaps': gaps,
                  'nbr_gaps': nbr_gaps,
                  'len_gaps': len_gaps,
                  'nbr_non_allowable_gaps': nbr_non_allowable_gaps,
                  'within_allowable_gaps': within_allowable_gaps,
                  'has_no_45_plus_day_gaps': has_no_45_plus_day_gaps,
                  'enrolled_at_measure_year_start': enrolled_at_measure_year_start,
                  'continuously_enrolled': continuously_enrolled,
        }
        pprint(params, sort_dicts=False)
        
    return continuously_enrolled
```

### Example Usage


```python
is_continuously_enrolled('111001011111111101110001')
```




    False




```python
is_continuously_enrolled('111001011111111101110001', verbose=True)
```

    {'sequence': '111001011111111101110001',
     'length_of_period': 24,
     'gaps': ['00', '0', '0', '000'],
     'nbr_gaps': 4,
     'len_gaps': [2, 1, 1, 3],
     'nbr_non_allowable_gaps': 2,
     'within_allowable_gaps': False,
     'has_no_45_plus_day_gaps': False,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': False}





    False



# Testing many scenarios

Here we test 24- and 12-character length sequences. 


```python
sequences = [
    '111001011111111101110001',    # => False; gaps>45 days, too many gaps
    '110111111111111111110111',    # => True; up to two allowable gaps (one per year)
    '110111111111111111100111',    # => False'; '00' non-allowable gap
    '111111111110111111111111',    # => True; December of Year 1 can be an allowable gap
    '111111111111011111111111',    # => False; member must be enrolled at start of measurement year (index 12)
    '111111111111111111111111',    # => True
    '000000000000000000000000',    # => False
    '111111111111',                # => True
    '000000000000',                # => False
    '111111100111',                # => False; '00' is non-allowable (>45 days)
    '111111101111',                # => True; within limits
    '110111101111',                # => False; no more than 1 allowable gap per year
    '011111111111',                # => False; member must be enrolled at start of measurement year
]

for idx,s in enumerate(sequences):
    print(f'id: {idx}')
    is_continuously_enrolled(s, verbose=True)
    print('-'*50)

# d = {s: is_continuously_enrolled(s) for s in sequences}    
```

    id: 0
    {'sequence': '111001011111111101110001',
     'length_of_period': 24,
     'gaps': ['00', '0', '0', '000'],
     'nbr_gaps': 4,
     'len_gaps': [2, 1, 1, 3],
     'nbr_non_allowable_gaps': 2,
     'within_allowable_gaps': False,
     'has_no_45_plus_day_gaps': False,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': False}
    --------------------------------------------------
    id: 1
    {'sequence': '110111111111111111110111',
     'length_of_period': 24,
     'gaps': ['0', '0'],
     'nbr_gaps': 2,
     'len_gaps': [1, 1],
     'nbr_non_allowable_gaps': 0,
     'within_allowable_gaps': True,
     'has_no_45_plus_day_gaps': True,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': True}
    --------------------------------------------------
    id: 2
    {'sequence': '110111111111111111100111',
     'length_of_period': 24,
     'gaps': ['0', '00'],
     'nbr_gaps': 2,
     'len_gaps': [1, 2],
     'nbr_non_allowable_gaps': 1,
     'within_allowable_gaps': False,
     'has_no_45_plus_day_gaps': False,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': False}
    --------------------------------------------------
    id: 3
    {'sequence': '111111111110111111111111',
     'length_of_period': 24,
     'gaps': ['0'],
     'nbr_gaps': 1,
     'len_gaps': [1],
     'nbr_non_allowable_gaps': 0,
     'within_allowable_gaps': True,
     'has_no_45_plus_day_gaps': True,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': True}
    --------------------------------------------------
    id: 4
    {'sequence': '111111111111011111111111',
     'length_of_period': 24,
     'gaps': ['0'],
     'nbr_gaps': 1,
     'len_gaps': [1],
     'nbr_non_allowable_gaps': 0,
     'within_allowable_gaps': True,
     'has_no_45_plus_day_gaps': True,
     'enrolled_at_measure_year_start': False,
     'continuously_enrolled': False}
    --------------------------------------------------
    id: 5
    {'sequence': '111111111111111111111111',
     'length_of_period': 24,
     'gaps': [],
     'nbr_gaps': 0,
     'len_gaps': [],
     'nbr_non_allowable_gaps': 0,
     'within_allowable_gaps': True,
     'has_no_45_plus_day_gaps': True,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': True}
    --------------------------------------------------
    id: 6
    {'sequence': '000000000000000000000000',
     'length_of_period': 24,
     'gaps': ['000000000000000000000000'],
     'nbr_gaps': 1,
     'len_gaps': [24],
     'nbr_non_allowable_gaps': 1,
     'within_allowable_gaps': False,
     'has_no_45_plus_day_gaps': False,
     'enrolled_at_measure_year_start': False,
     'continuously_enrolled': False}
    --------------------------------------------------
    id: 7
    {'sequence': '111111111111',
     'length_of_period': 12,
     'gaps': [],
     'nbr_gaps': 0,
     'len_gaps': [],
     'nbr_non_allowable_gaps': 0,
     'within_allowable_gaps': True,
     'has_no_45_plus_day_gaps': True,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': True}
    --------------------------------------------------
    id: 8
    {'sequence': '000000000000',
     'length_of_period': 12,
     'gaps': ['000000000000'],
     'nbr_gaps': 1,
     'len_gaps': [12],
     'nbr_non_allowable_gaps': 1,
     'within_allowable_gaps': False,
     'has_no_45_plus_day_gaps': False,
     'enrolled_at_measure_year_start': False,
     'continuously_enrolled': False}
    --------------------------------------------------
    id: 9
    {'sequence': '111111100111',
     'length_of_period': 12,
     'gaps': ['00'],
     'nbr_gaps': 1,
     'len_gaps': [2],
     'nbr_non_allowable_gaps': 1,
     'within_allowable_gaps': False,
     'has_no_45_plus_day_gaps': False,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': False}
    --------------------------------------------------
    id: 10
    {'sequence': '111111101111',
     'length_of_period': 12,
     'gaps': ['0'],
     'nbr_gaps': 1,
     'len_gaps': [1],
     'nbr_non_allowable_gaps': 0,
     'within_allowable_gaps': True,
     'has_no_45_plus_day_gaps': True,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': True}
    --------------------------------------------------
    id: 11
    {'sequence': '110111101111',
     'length_of_period': 12,
     'gaps': ['0', '0'],
     'nbr_gaps': 2,
     'len_gaps': [1, 1],
     'nbr_non_allowable_gaps': 0,
     'within_allowable_gaps': False,
     'has_no_45_plus_day_gaps': True,
     'enrolled_at_measure_year_start': True,
     'continuously_enrolled': False}
    --------------------------------------------------
    id: 12
    {'sequence': '011111111111',
     'length_of_period': 12,
     'gaps': ['0'],
     'nbr_gaps': 1,
     'len_gaps': [1],
     'nbr_non_allowable_gaps': 0,
     'within_allowable_gaps': True,
     'has_no_45_plus_day_gaps': True,
     'enrolled_at_measure_year_start': False,
     'continuously_enrolled': False}
    --------------------------------------------------


# End
