# Wage workshop data dictionary

Each row is one person in the workshop extract.

| Column | Meaning |
| --- | --- |
| `record_id` | Code identifying one survey record in this file |
| `age` | Age in years |
| `sex` | Recorded sex, Female or Male |
| `education_code` | Highest education group |
| `weekly_hours` | Usual hours worked per week. The survey records 99 or more as 99. |
| `weekly_wage` | Average wage and salary earnings per week worked, in US dollars |

| Education code | Group |
| --- | --- |
| 1 | Up to high school, including workers without a diploma |
| 2 | Bachelor’s degree |
| 3 | Postgraduate degree, including master’s, professional and doctoral degrees |

The extract covers civilians aged 25–64 in these three groups. It includes
people who did not work during the reference period. A blank weekly value
means the survey did not provide the weeks or hours needed for that measure.
Zero weekly pay means the person worked during the period and had no wage
and salary earnings in the survey.

Some college and associate degrees fall outside the three groups.
