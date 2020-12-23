'''
:description: This program reads data from xml file and creates pandas DataFrame object 
:author: Sławomir Kwiatkowski
:date: 2020-12-23 
'''
import xml.dom.minidom
from collections import defaultdict
import pandas as pd

persons = defaultdict(list)
with xml.dom.minidom.parse(open('persons.xml')) as tree:
    persons_list = tree.getElementsByTagName('person')
    for person in persons_list:
        persons['id'].append(person.getAttribute('id'))
        for tag in ('position', 'first_name', 'last_name', 'email', 'salary'):
            persons[tag].append(person.getElementsByTagName(tag)[0].firstChild.data)


df = pd.DataFrame(persons, columns=persons.keys()).set_index('id')
df['salary'] = df['salary'].astype(float)
print(df.sort_values(by='salary', ascending=False))