# Wage workshop data dictionary

Each row is one person in a teaching extract from the March 2005 US Current
Population Survey. Pay and work hours refer to 2004.

| Column | Meaning |
| --- | --- |
| `record_id` | Code identifying one survey record in this file |
| `age` | Age in years |
| `sex` | Recorded sex, Female or Male |
| `education_code` | Highest education group. Use the codes below. |
| `weekly_hours` | Usual hours worked per week. The survey records 99 or more as 99. |
| `weekly_wage` | Average wage and salary earnings per week worked, in 2004 US dollars |

| Education code | Group |
| --- | --- |
| 1 | Up to high school, including workers without a diploma |
| 2 | Bachelor’s degree |
| 3 | Postgraduate degree, including master’s, professional and doctoral degrees |

The extract covers civilians aged 25–64 in these three groups. It includes
people who did not work in 2004. A blank weekly value means the survey did
not provide the weeks or hours needed for that measure. Zero weekly pay
means there were weeks worked but no wage and salary earnings in the survey.

Some college and associate degrees fall outside the three groups.

## Source notes

The download comes from the [Census Bureau’s March 2005 CPS ASEC
release](https://www.census.gov/data/datasets/2005/demo/cps/cps-asec-2005.html).
The preparation script divides annual wage and salary income by weeks worked
to get weekly pay. The hours field can include work beyond wage and salary
employment, so dividing pay by hours gives an estimate of hourly wages.
The CSV has 77,537 records.
The selected analysis sample is described without survey weights.
[Original Census data dictionary](https://www2.census.gov/programs-surveys/cps/techdocs/cpsmar05.pdf).
