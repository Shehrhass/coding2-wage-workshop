# Wage workshop data dictionary

Each row is one person in the workshop extract.

| Column | Meaning |
| --- | --- |
| `record_id` | Code identifying one survey record in this file |
| `age` | Age in years |
| `sex` | Recorded sex, Female or Male |
| `education_code` | Highest education group |
| `hours` | Usual hours worked per week. The survey records 99 or more as 99. |
| `wage` | Average wage and salary earnings per week worked, in US dollars |
| `roster_line` | Person's line number on the household survey roster (`A-LINENO`) |
| `survey_month_in_sample` | Household's position in the survey interview sequence, from 1 to 8 (`H-MIS`) |
| `housing_tenure_code` | 1 = owned or being bought, 2 = rented, 3 = no cash rent (`H-TENURE`) |

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
