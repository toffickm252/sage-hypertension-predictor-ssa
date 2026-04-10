## Preprocessing Summary

**Input:** Ghana (5,573) + South Africa (4,227) = 9,800 respondents
**Output:** Combined clean dataset of 8,887 respondents, 29 variables

### Steps Performed

1. Replaced blank spaces and -8 codes with NaN
2. Dropped rows missing blood pressure readings (6.2% of data)
3. Converted all string columns to numeric types
4. Filled skip logic nulls with 0 (current_tobacco, recent_alcohol,
   avg_drinks_daily, days_vigorous_work)
5. Imputed body measurements and diet variables with column median
6. Imputed sex and residence with column mode
7. Dropped rows with missing survey_weight
8. Added birth_year as NaN to South Africa to maintain structure
9. Combined Ghana and South Africa into single dataframe

### Remaining Nulls

- birth_month and birth_year — handled in feature engineering
  when age is calculated

### Country Codes

- 241 = Ghana (4,960 respondents)
- 155 = South Africa (3,927 respondents)
