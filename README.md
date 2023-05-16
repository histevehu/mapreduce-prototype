# MapReduce-Prototype
This repository stores the code implementation of Task B part of the Big Data and Cloud Computing curriculum.
## Objective
Simulate a MapReduce/Hadoop framework approach to analyze a dataset containing passengers flying between airports in a given period and determine the passenger having had the highest number of flights.
## Run
Run `passenger_analysis.py` to count the number of flights for each passenger in `input_files/data.csv`, which is also the sample code for this MapReduce implementation.

***Note: This implementation may produce wrong results in Windows environment, thus it is only allowed to run in Linux environments.***
## Usage
This implementation has a class-based hierarchy and is therefore generic. Simply create a class that inherits from the `MapReduce` class and override the `mapper` and `reducer` methods in it to implement your own specific requirements. This MapReduce implementation will do your job.
