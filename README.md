Jorden Allcock
Repository for Third Year Final Project

---------------------------------------------------------------------------------------------------------------

Installation Instructions:

1. CentOS 7 Install
2. MySql Install
3. Python Install
4. Python Packages Install
5. Git Install
6. Code Pull from Git

Flow of Operation:

	| 1. resource_request_analysis.py	| Analyses the contents a the resource request submitted by Capgemini Manager using the standardised form
	| 2. skill_db_extract.py		| Pulls information from DB in regards to the associated skills for the identified role 
	| 3. cv_link_pull.py			| Pulls information from specified live career resume search url  
	| 4. cv_process.py			| Formats the extracted CV information into a Human Readable format
	| 5. cv_resource_process.py		| Inspects CV's and selects those that match with specified keywords.
	|					| CV's are selected ready for further analysis
	| 6. 


CV Analysis Routines:

There exists multiple files, each designed to perform CV analysis using its own distinct methodology. An overview of each file is as below:

	| 1. cv_match_keyword.py		| Analyses the resource request and selects initial keywords
	| 					| Keywords are also extracted from pre-formatted CV's at runtime
	|					| Matches are returned based on exact matches between resource request and cv
	| 2. cv_match_word_vectors.py		| Analyses the resource request and selects initial keywords
	| 					| Analyses the pre-formatted CV's and extracts keywords
	| 					| Runs a spacy similarity on the identified keywords in the resource request and the CV to determine 
	|					| extent of match
	| 3. cv_match_  
