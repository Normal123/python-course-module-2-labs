##Laboratory Work 2.5

####Description

Write the code to do following: 
* create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA} 
* create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
* add one more element to each dict above 
* print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts
* print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts 
* Merge sentences above together with one cycle 
* Add to each value of first dict another two domains: COM and GOV

Here is its solution code:
 *solution_2_5.py*
```python
"""
create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA}
"""
countries={'Spain': 'SP', 'Germany': 'D', 'Ukraine': 'UA', 'Russia': 'RU', 'Moldova': 'MD'}
"""
create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
"""
capitals={'SP': 'Madrid' , 'D': 'Berlin', 'UA': 'Kiev', 'RU': 'Moskov', 'MD': 'Kishinev'}
"""
add one more element to each dict above
"""
countries.update({'Poland': 'PL'})
capitals.update({'PL': 'Varshava'})
"""
print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts
"""
for key, value in countries.items():
    print("Domain for {} is {}.".format(key, value))
"""
print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts
"""
for key, value in capitals.items():
    print("The capital of{} is {}.".format(key, value))
"""
Merge sentences above together with one cycle
"""
for key, value in countries.items():
    print ("Domain for {} is {}. The capital is {}"
           .format(key, value, capitals[value]))
"""
Add to each value of first dict another two domains: COM and GOV
"""
for key, value in countries.items():
    countries[key]=[value, 'COH', 'GOV']

for key, value in countries.items():
    print("Domain for {} is {}.The capital is {}"
          .format(key, value, capitals[value[0]]))
