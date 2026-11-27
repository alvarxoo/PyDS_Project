# Data dictionary

**File:** `data/raw/student-portugales.csv` · **Source:** University of California· **One row \=** `['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3']` · **Rows:** 649  **Columns:** 33 (only 9 used)

| Column | Meaning | Type in Python | Unit / values | Used? | Why (for our question) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| address | student's home address type&nbsp; | str | (binary: 'U' \- urban or 'R' \- rural) | yes | Infer relation between living area and final grade |
| famsize | family size | str | &nbsp;(binary: 'LE3' \- less or equal to 3 or 'GT3' \- greater than 3\)&nbsp;&nbsp; | yes | bigger families linked with lower grades |
| Medu | mother's education&nbsp; | int | (numeric: 0 \- none, 1 \- primary education (4th grade), 2 \- 5th to 9th grade, 3 \- secondary education or 4 \- higher education)&nbsp;&nbsp; | yes | higher level of education in parents giving better chances of higher grades for their children |
| Fedu | father’s education | int | (numeric: 0 \- none, 1 \- primary education (4th grade), 2 \- 5th to 9th grade, 3 \- secondary education or 4 \- higher education)&nbsp;&nbsp; | yes | higher level of education in parents giving better chances of higher grades for their children |
| studytime | weekly study time&nbsp; | int | &nbsp;(numeric: 1 \- \<2 hours, 2 \- 2 to 5 hours, 3 \- 5 to 10 hours, or 4 \- \>10 hours) | yes | higher study time related with higher grades |
| schoolsup | extra educational support&nbsp; | bool | (binary: yes or no)&nbsp; | yes | extra educational support related with higher grades |
| Walc | weekend alcohol consumption&nbsp; | int | (numeric: from 1 \- very low to 5 \- very high)&nbsp; | yes | higher Walc related with lower grades |
| absences | number of school absences&nbsp; | int | (numeric: from 0 to 93\)&nbsp; | yes | higher absences related with lower grades |
| G3 | final grade&nbsp; | int | (numeric: from 0 to 20, output target)&nbsp; | yes | the main analysing point |

Missing or strange values noticed: None
