"""

Table: Courses

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
 

Write a solution to find all the classes that have at least five students.

Return the result table in any order.

The result format is in the following example.


Example 1:

Input: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+

Output: 
+---------+
| class   |
+---------+
| Math    |
+---------+

Explanation: 
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.

"""

# The code groups the 'courses' DataFrame by the 'class' column and counts the occurrences of each class.  
# It then filters out classes that appear fewer than 5 times, keeping only those with at least 5 occurrences.  
# Finally, it returns a DataFrame containing only the 'class' column for the remaining classes.  


import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    
    df = courses.groupby('class').size().reset_index(name='count')

    df = df[df['count'] >= 5]

    return df[['class']]
