# Project concept

Fill in every section. Write for a person who knows nothing about your topic.

## 1\. Topic

Our project consists of an analysis of various environmental and conduct matters involving the students, in particular, we will study how these affect the student performance.

## 2\. Problem

The comparison between contextual matters and personal habits will allow us to understand if it is more impactful, in terms of final grade, how you spend your personal time or the conditions in which you are living.

## 3\. Goal of the analysis – the question

The mean grade of students in each of the categories in which they are divided by several statistics such as weekend alcohol consumption, parents education, living zone, number of absences…

## 4\. Data source

Name: Student Performance in Portuguese class  
Link: [Student Performance \- UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance)&nbsp;  
who created it: UC Irvine  
Rows: 649  
Columns: 33

One row: `['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3']`&nbsp;

This data approaches student achievement in secondary education of two Portuguese schools. The data attributes include student grades, demographic, social and school related features) and it was collected by using school reports and questionnaires. Two datasets are provided regarding the performance in two distinct subjects: Mathematics (mat) and Portuguese language (por). In \[Cortez and Silva, 2008\], the two datasets were modeled under binary/five-level classification and regression tasks. For our study we will be focusing on the Portuguese dataset.

## 5\. Expected results

A comparison of correlation for the different statistics

## 6\. How you will present it

Which plots / tables, and one sentence for a non-expert: "Our analysis shows that …"

We will use several tables showing the mean grade and the number of cases per group for each statistic, and we will also plot these data. We will then rank the associations, using the p-values from a least squares regression analysis as indicators.&nbsp;

Our analysis will show whether context or habits have more impact on students' grades.

## 7\. Team and split of work

Alvaro: loader,

Maite: stats, cleaning, storage

Laia: models,

&nbsp;

Team: main