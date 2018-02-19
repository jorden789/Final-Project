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
7. Overview of Files

-----------------------------
Section 1 - CentOS 7 Install
-----------------------------

-----------------------------
Section 2 - MySQL Install
-----------------------------


-----------------------------
Section 3 - Python Install 
-----------------------------


-----------------------------------
Section 4 - Python Packages Install
-----------------------------------


-----------------------------
Section 5 - Git Install
-----------------------------


------------------------------
Section 6 - Code Pull form Git
------------------------------



-----------------------------
Section 7 - Overview of Files
-----------------------------

The CV/Resource Matching Deliverable consists of multiple files in order to ensure promised functionality. The specifics of each file are detailed below as well as how each file is run:

Flow of Operation for Batch Processing

	The below files are responsible for pulling in new CV information and processing that information for computational processing ready for the next working day's ad-hoc queries.

        | 1. cv_link_pull.py                    | Pulls information from specified live career resume search url
        | 2. cv_process.py                      | Formats the extracted CV information into a Human Readable format
 
Flow of Operation for Ad-Hoc Processing:

	cv_resource_process is the master Python script which needs to be called whenever a Resource Request needs to be analysed. To run this script, a full file path needs to be
	specified.

	| 1. cv_resource_process.py		| Analyses the contents a the resource request submitted by Capgemini Manager using the standardised form
	|					| Calls the Python Scripts below to control processing
	|					| Parameters - Resource Request Location
	| 2. cv_match_keyword.py		| Identifies keywords and similar alternatives within the resource request, returns similarity scores of
	|					| keywords and the identified exact/similar match within the resource request and CV pairing
	| 3. cv_resource_scoring.py		| Assigns a score to the cv/resource request pairing dependent on the level of matching
	| 4. candidate_assignment.py		| Ranks the candidates and matches the best candidates to the specified resource request
	|					| (scope for multi-request processing)
	| 5. deliver_results.py			| Outputs the results in a user-friendly format

Misc Processing

	| 1. skill_db_extract.py		| Pulls information from DB in regards to the associated skills for the identified role 


	
