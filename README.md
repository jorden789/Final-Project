Jorden Allcock
Repository for Third Year Final Project

---------------------------------------------------------------------------------------------------------------

Installation Instructions:

1. User Setup
2. Environment Setup
3. Python Install
4. Python Packages Install
5. Git Install
6. Code Pull from Git
7. Overview of Files

-----------------------------
- CentOS 7 Server 
- SSH Access to CentOS 7 Server
-----------------------------

-----------------------------
Section 1 - User Setup
-----------------------------

As root user, run the following commands (the prototype is hardcoded to a single user):

	useradd jallcock
	passwd jallcock

When 'New Password' and 'Retype new password' lines are shown, enter a memorable value.

Before switching to the new user, we need to add user to sudoers file so that it can install programs, like so:

	usermod -aG wheel jallcock

Remainder of the setup will be performed as user 'jallcock' therefore:

	su - jallcock

Whenever a password is required for a command that begins sudo, use the password you have setup for the jallcock
user.

-----------------------------
Section 2 - Environment Setup
-----------------------------

The 'environments' folder needs to be setup within the home directory of 'jallcock':

	mkdir environments
	cd environments

Now that we are in the environments directory, we can proceed with installing the appropriate tools required for
system operation.

To install further elements of the system, we need to ensure the YUM package manager is up to date:

	sudo yum -y update
        sudo yum -y install yum-utils
        sudo yum groupinstall development
	sudo yum -y install python36u-devel
	sudo yum -y install libevent-devel

A text editor needs to be installed, for this project, NANO has been the editor of choice, this can be installed
like so:

	sudo yum -y install nano

-----------------------------
Section 3 - Python Install 
-----------------------------

Python v.3 is the language the prototype has been developed in, therefore we need to install Python 3, like so:

	sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
	sudo yum -y install python36u

We can check that Python 3 has been installed properly by running the below command:

	python -V

If the below shows Python 2.7.#, the check using:

	python3.6 -V

If python3.6 shows a version relating to python3, the we can edit the bash profile settings to default python to 
python 3:

	nano ~/.bashrc

Add the following line to this file:

	alias python=python3.6

Save and close the file by issing the below key presses:

	CTRL + X
	Y
	ENTER

Then perform the following command at command line prompt:

	source ~/.bashrc

Running python -V now should show version 3 of python.

-----------------------------------
Section 4 - Python Packages Install
-----------------------------------

pip is a package manager for Python which enables easy package install for the various libraries that this prototy-
pe makes use of, to install, issue the following:

	sudo yum -y install python36u-pip

The prototype makes use of various python packages, therefore the following commands need to be run to install them:

	sudo pip3.6 install munkres
        sudo pip3.6 install spacy
        sudo pip3.6 install xlrd 

The appropriate languages model needs to be installed with SpaCy, like so:

	sudo python3.6 -m spacy download en

-----------------------------
Section 5 - Git Install
-----------------------------

Sections 5 and 6 are not essential as files can be uploaded via WinSCP SSH Connection to server, however repository
is version controlled. To install the GIT command line tools:

	sudo yum -y install git
	git --version

The last command should show a version number if successfully installed.	

------------------------------
Section 6 - Code Pull form Git
------------------------------

The source code repository is available at https://github.com/jorden789/Final-Project. The repo can be downloaded
by issuing:

	git clone https://github.com/jorden789/Final-Project.git

-----------------------------
Section 7 - Overview of Files
-----------------------------

The CV/Resource Matching Deliverable consists of multiple files in order to ensure promised functionality. The specifics of each file are detailed below as well as how each file is run:

Flow of Operation for Batch Processing

	The below files are responsible for pulling in new CV information and processing that information for computational processing ready for the next working day's ad-hoc queries.

        | 1. cv_link_pull.py                    | Pulls information from specified live career resume search url
	|					| Run as 'python3.6 cv_link_pull https://resumes.livecareer.com/search?jt=software%20engineering'
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




	
