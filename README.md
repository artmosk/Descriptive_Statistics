#### Task:
:question:
Determine which countries are most profitable to show banner ads. We have a log file with information on payments for banner in a specific country. The customer needs to calculate simple aggregate statistics on log file.

#### Decision:
:exclamation:
To use MapReduce paradigm in collecting statistics.
More infromation about programming model you can find [here](https://en.wikipedia.org/wiki/MapReduce)

#### Files:
Name | Description
-----|------------
advert.log | log file
mapper.py | read lines script
reducer.py | statistics script
