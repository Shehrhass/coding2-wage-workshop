# Wage workshop data dictionary

Each row is one person in the workshop extract.

| Column | Meaning |
| --- | --- |
| `record_id` | Code identifying one survey record in this file |
| `age` | Age in years |
| `sex` | Sex recorded in the survey, Female or Male (`A-SEX`) |
| `education_code` | Highest education group |
| `hours` | Usual hours worked per week. The survey records 99 or more as 99. |
| `wage` | Average wage and salary earnings per week worked, in US dollars |
| `roster_line` | Number assigned to the person on their household's survey roster (`A-LINENO`) |
| `survey_month_in_sample` | Which of the household's eight scheduled interview rounds this record comes from (1–8, `H-MIS`) |
| `housing_tenure_code` | How the household occupies its home (`H-TENURE`). 1 = owns or is buying, 2 = rents, 3 = pays no cash rent |

| Education code | Group |
| --- | --- |
| 1 | Up to high school, including workers without a diploma |
| 2 | Bachelor’s degree |
| 3 | Postgraduate degree, including master’s, professional and doctoral degrees |

The extract covers civilians aged 25–64 in these three groups, including
people who did not work during the reference period. A blank weekly value
means the survey did not provide the weeks or hours needed for that measure.
Zero weekly pay means the person worked during the period and had no wage
and salary earnings in the survey.

[Original Census field definitions, chapter 8](https://www2.census.gov/programs-surveys/cps/techdocs/cpsmar05.pdf)
