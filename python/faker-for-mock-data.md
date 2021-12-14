Generate fake data with Faker package.

References:<br>
https://pypi.org/project/Faker/

# Code
```python

import pandas as pd
import numpy as np
from faker import Faker

def main():
    risk_quality_patient_data = make_risk_quality_patient_data(n=1000)
    measure_data = make_quality_measure_data(n=1000)
    
def make_risk_quality_patient_data(n=10):
    fake = Faker()
    data = []

    for i in range(n):
        row = {'practice_name': fake.company(), 
               'provider_id': str(np.random.randint(0, 1000000000)).zfill(9),       
               'provider_name': fake.name(), 
               'patient_id': str(np.random.randint(0, 1000000000)).zfill(9), 
               'patient_name': fake.name(), 
               'dob': fake.date_of_birth(), 
               'care_gaps': np.random.randint(0, 10),
               'suspected_dxs': np.random.randint(0, 10),           
               'suspected_dxs_assessed': np.random.randint(0, 10),                      
               'raf_priority': np.random.choice(['High', 'Medium', 'Low'])}

        data.append(row)

    return pd.DataFrame(data)

def make_quality_measure_data(n=10):
    fake = Faker()
    data = []
    
    measure_names = ['Adherence to Antipsychotic Medications for Individuals With Schizophrenia', 'Adult Access to Preventive or Ambulatory Health Services', 'Annual Dental Visit', 'Antidepressant Medication Management: Acute', 'Antidepressant Medication Management: Continuation', 'Appropriate Testing for Pharyngitis', 'Appropriate Treatment for Upper Respiratory Infection', 'Asthma Medication Ratio', 'Avoidance of Antibiotic Treatment for Acute Bronchitis or Bronchiolitis', 'Breast Cancer Screening', 'Cardiac Rehabilitation: Achievement', 'Cardiac Rehabilitation: Engagement 1', 'Cardiac Rehabilitation: Engagement 2', 'Cardiac Rehabilitation: Initiation', 'Cardiovascular Monitoring for People With Cardiovascular Disease and Schizophrenia', 'Care for Older Adults: Advance Care Planning', 'Care for Older Adults: Functional Status Assessment', 'Care for Older Adults: Medication Review', 'Care for Older Adults: Pain Assessment', 'Cervical Cancer Screening', 'Child and Adolescent Well Care Visits', 'Childhood Immunization Status: Combination 10', 'Childhood Immunization Status: Combination 2', 'Childhood Immunization Status: Combination 3', 'Childhood Immunization Status: Combination 4', 'Childhood Immunization Status: Combination 5', 'Childhood Immunization Status: Combination 6', 'Childhood Immunization Status: Combination 7', 'Childhood Immunization Status: Combination 8', 'Childhood Immunization Status: Combination 9', 'Childhood Immunization Status: DTaP', 'Childhood Immunization Status: Hepatitis A', 'Childhood Immunization Status: Hepatitis B', 'Childhood Immunization Status: HiB', 'Childhood Immunization Status: IPV', 'Childhood Immunization Status: Influenza', 'Childhood Immunization Status: MMR', 'Childhood Immunization Status: Pneumococcal conjugate', 'Childhood Immunization Status: Rotavirus', 'Childhood Immunization Status: VZV', 'Chlamydia Screening in Women', 'Colorectal Cancer Screening', 'Comprehensive Diabetes Care: BP Control Less Than 140 over 90 mm Hg', 'Comprehensive Diabetes Care: Eye Exam', 'Comprehensive Diabetes Care: HbA1c Control Greater Than 9 Percent', 'Comprehensive Diabetes Care: HbA1c Control Less Than 8 Percent', 'Comprehensive Diabetes Care: HbA1c Testing', 'Comprehensive Diabetes Care: Medical Attention for Nephropathy', 'Controlling High Blood Pressure', 'Diabetes Monitoring for People With Diabetes and Schizophrenia', 'Diabetes Screening for People With Schizophrenia or Bipolar Disorder Who Are Using Antipsychotic Medications', 'Disease Modifying Anti Rheumatic Drug Therapy for Rheumatoid Arthritis', 'Follow Up After Emergency Department Visit for Alcohol and Other Drug Abuse or Dependence: 30 Day Follow Up', 'Follow Up After Emergency Department Visit for Alcohol and Other Drug Abuse or Dependence: 7 Day Follow Up', 'Follow Up After Emergency Department Visit for Mental Illness: 30 Day Follow Up', 'Follow Up After Emergency Department Visit for Mental Illness: 7 Day Follow Up', 'Follow Up After Emergency Department Visit for People With Multiple High Risk Chronic Conditions', 'Follow Up After High Intensity Care for Substance Use Disorder: 30 Day Follow Up', 'Follow Up After High Intensity Care for Substance Use Disorder: 7 Day Follow Up', 'Follow Up After Hospitalization for Mental Illness: 30 Day Follow Up', 'Follow Up After Hospitalization for Mental Illness: 7 Day Follow Up', 'Follow Up Care for Children Prescribed ADHD Medication: Continuation and Maintenance', 'Follow Up Care for Children Prescribed ADHD Medication: Initiation', 'Immunizations for Adolescents: Combination 1', 'Immunizations for Adolescents: Combination 2', 'Immunizations for Adolescents: HPV', 'Immunizations for Adolescents: Meningococcal', 'Immunizations for Adolescents: Tdap', 'Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment: Alcohol Abuse or dependence: Engagement', 'Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment: Alcohol Abuse or dependence: Initiation', 'Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment: Opioid Abuse or dependence: Engagement', 'Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment: Opioid Abuse or dependence: Initiation', 'Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment: Other Drug Abuse or dependence: Engagement', 'Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment: Other Drug Abuse or dependence: Initiation', 'Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment: Total Engagement', 'Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment: Total Initiation', 'Kidney Health Evaluation for Patients With Diabetes', 'Lead Screening in Children', 'Metabolic Monitoring for Children and Adolescents on Antipsychotics: Blood Glucose', 'Metabolic Monitoring for Children and Adolescents on Antipsychotics: Blood Glucose and Cholesterol', 'Metabolic Monitoring for Children and Adolescents on Antipsychotics: Cholesterol', 'Non Recommended Cervical Cancer Screening in Adolescent Females', 'Non Recommended PSA Based Screening in Older Men', 'Osteoporosis Management in Women Who Had a Fracture', 'Osteoporosis Screening in Older Women', 'Persistence of Beta Blocker Treatment After a Heart Attack', 'Pharmacotherapy Management of COPD Exacerbation: Bronchodilator', 'Pharmacotherapy Management of COPD Exacerbation: Systemic Corticosteroid', 'Potentially Harmful Drug Disease Interactions in the Elderly: Chronic Kidney Disease', 'Potentially Harmful Drug Disease Interactions in the Elderly: Dementia', 'Potentially Harmful Drug Disease Interactions in the Elderly: History of Falls', 'Prenatal and Postpartum Care: Postpartum', 'Prenatal and Postpartum Care: Prenatal', 'Risk of Continued Opioid Use: At least 15 days covered', 'Risk of Continued Opioid Use: At least 31 days covered', 'Statin Therapy for Patients With Cardiovascular Disease: Statin Therapy', 'Statin Therapy for Patients With Cardiovascular Disease: Statin Therapy Adherence 80 Percent', 'Statin Therapy for Patients With Diabetes: Statin Therapy', 'Statin Therapy for Patients With Diabetes: Statin Therapy Adherence 80 Percent', 'Transitions of Care: Engagement', 'Transitions of Care: Medication Reconciliation', 'Use of First Line Psychosocial Care for Children and Adolescents on Antipsychotics', 'Use of High-Risk Medications in Older Adults: High Risk Medications to Avoid', 'Use of High-Risk Medications in Older Adults: High Risk Medications to Avoid Except for Appropriate Diagnosis', 'Use of Imaging Studies for Low Back Pain', 'Use of Opioids From Multiple Providers: Multiple Pharmacies', 'Use of Opioids From Multiple Providers: Multiple Prescribers', 'Use of Opioids From Multiple Providers: Multiple Prescribers and Multiple Pharmacies', 'Use of Opioids at High Dosage', 'Use of Spirometry Testing in the Assessment and Diagnosis of COPD', 'Weight Assessment and Counseling for Nutrition and Physical Activity for Children Adolescents: BMI Percentile', 'Weight Assessment and Counseling for Nutrition and Physical Activity for Children Adolescents: Counseling for Nutrition', 'Weight Assessment and Counseling for Nutrition and Physical Activity for Children Adolescents: Counseling for Physical Activity', 'Well Child Visits in the First 30 Months of Life: 15 to 30 months', 'Well Child Visits in the First 30 Months of Life: First 15 Months']

    for i in range(n):
        row = {'practice_name': fake.company(), 
               'provider_id': str(np.random.randint(0, 1000000000)).zfill(9),       
               'provider_name': fake.name(), 
               'patient_id': str(np.random.randint(0, 1000000000)).zfill(9), 
               'patient_name': fake.name(), 
               'dob': fake.date_of_birth(), 
               'measure_name': np.random.choice(measure_names),
               'numerator': np.random.randint(0, 2),  
               'denominator': 1,
              }
        data.append(row)

    df1 = pd.DataFrame(data)
    df2 = df1.copy().assign(measure_name=[np.random.choice(measure_names) for n in range(n)])
    df3 = df1.copy().assign(measure_name=[np.random.choice(measure_names) for n in range(n)])
    measure_data = pd.concat([df1, df2, df3])
    
    return measure_data
    
main()
    
```

# Output

|    | practice_name            |   provider_id | provider_name   |   patient_id | patient_name      | dob        |   care_gaps |   suspected_dxs |   suspected_dxs_assessed | raf_priority   |
|---:|:-------------------------|--------------:|:----------------|-------------:|:------------------|:-----------|------------:|----------------:|-------------------------:|:---------------|
|  0 | Brown-Nichols            |     148975802 | Guy Walters     |    859588038 | Andrea West       | 2017-10-10 |           6 |               1 |                        2 | High           |
|  1 | Beck, Bailey and Young   |     522804762 | Steven Curry    |    924444036 | Joseph Davidson   | 2013-04-19 |           7 |               0 |                        4 | High           |
|  2 | Ford, Patton and Rogers  |     079711594 | Shawn Clark     |    729774849 | Stephen Davenport | 1975-12-20 |           2 |               4 |                        6 | Medium         |
|  3 | Aguilar-Gomez            |     603932243 | Maria Williams  |    800467425 | Robert Boyer      | 1918-06-30 |           7 |               9 |                        5 | Low            |
|  4 | Morris, Rush and Jimenez |     457590452 | Emily Berry     |    063837417 | Shannon Rodriguez | 1922-09-11 |           0 |               9 |                        6 | Low            |

|    | practice_name            |   provider_id | provider_name   |   patient_id | patient_name    | dob        | measure_name                                                                                                                    |   numerator |   denominator |
|---:|:-------------------------|--------------:|:----------------|-------------:|:----------------|:-----------|:--------------------------------------------------------------------------------------------------------------------------------|------------:|--------------:|
|  0 | Gilmore, Perez and Klein |     986262513 | Gregory Edwards |    393378058 | Samantha Macias | 1939-08-22 | Childhood Immunization Status: Combination 2                                                                                    |           0 |             1 |
|  1 | Villarreal-Carter        |     672739861 | Lindsay Shaffer |    174612393 | James Austin    | 1940-08-05 | Pharmacotherapy Management of COPD Exacerbation: Bronchodilator                                                                 |           1 |             1 |
|  2 | Allen, Howell and Moreno |     101776841 | Karen Blake     |    657645288 | Nina Pham       | 1972-01-21 | Weight Assessment and Counseling for Nutrition and Physical Activity for Children Adolescents: Counseling for Physical Activity |           1 |             1 |
|  3 | Smith-Jackson            |     818157585 | Julie Pratt     |    436452093 | Latoya Roberts  | 2007-08-27 | Follow Up Care for Children Prescribed ADHD Medication: Initiation                                                              |           0 |             1 |
|  4 | Washington-Dorsey        |     078775020 | Cathy Thomas    |    695200035 | Erin Rogers     | 1975-05-19 | Comprehensive Diabetes Care: Medical Attention for Nephropathy                                                                  |           1 |             1 |
