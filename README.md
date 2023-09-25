# Trendsetter Project

## Overview
Participants coordinate with three others (groups of 4) to solve a graph coloring problem.
- This means each round they select a color and get a payoff based on their selection and the decisions of others.
- The idea is they have to figure out how to coordinate on the best color.

There are four types of networks. Complete, circle, star, and line. Each network has a different level of visibility, meaning that participants can only see the decisions of a different number of group members.

There are 6 blocks of 10 rounds. 

In the first block, participants are led to select yellow, which results in a payoff of 12. All other selectios result in a payoff of 0.

In the second block, the participants are given the opportunity to earn more than 12. This is the key part of the experiment: *they are induced into a suboptimal equilibrium and then given the opportunity to get to the optimal equilibrium*

### Dependencies

**See requirements.txt**

- OTree
- Python 3.11.2
	- Use Anaconda for dependency management

### Deployment Instructions

- open a terminal file inside the trendsetter folder
	- If environment is not built:
		- create the environment "conda env create -f environment.yml"
			- this requires that anaconda is installed as well as python 3.11
- activate the environment "conda activate trendenv"
	- if otree not installed
		- install otree "pip3 install -U otree"
- Once you are ready, call "otree zip"
- Log into Heroku
	- this step is only necessary to check on the server itself. This is where the hosting is, but for some reason the actual deployment is done through OTreehub (it could also be done through github)
- Log into OTreehub
- Go to "Deploy to Heroku", and select your server
	- I have created a development server, but it requires the setup of 2 addons (DB and another) as turning on "dynos" in order to function
	- Click "deploy"
- Upload your otreezip file and it will restart the server
- Click "reset DB"
	- **note: This will irreversibly delete all of the current data in the DB**
		- the DB plan that we are currently using has a limit of 10k rows. We hit that in ~1 year (maybe less, but it resets with each DB reset) and were at risk of the DB no longer writing. Just keep that in mind when you are working. This can be checked by clicking the Postgres add-on in Heroku
		- Jack warned me that the DB can sometimes time out and cause an error which requires the DB to be reset. If you see such an error, reset the DB (I wonder if this and the above point are related).
		- You’ll have to regenerate the links if you reset the database

## Notes on OTree, OTreehub, and Heroku

- When deploying from OTreehub, you must choose that the code is public, or I presume they make you pay.
	- For that reason, demo always needs to be turned on. Just keep that in mind.
		- I realize that last point is not helpful. I can't confirm exactly what the name is without resetting the server and I really don't want to do that.
- When testing, the DB is sqlite, when uploaded the DB is Postgresql
	- heroku handles this, but it is good to know
	- when looking through the test, the app will warn you that you are using the wrong kind of DB. When published, this error goes away.
- OTreehub only allows you to link to two Heroku severs for free. They even recommend that you change an existing server into a new project instead of making a new server.
- For future reference, OTree strongly recommends using its built in editor to create games instead of using the format of this experiment.
	- The documentation for making a local devserver is here: https://otree.readthedocs.io/en/latest/install-nostudio.html#install-nostudio
- in Heroku app "Settings" there are a number of "Config Vars" that are important to note:
	- this includes OTREE_ADMIN_PASSWORD
	- OTREE_PRODUCTION - can be 1 or 0, set to 1 on prodserver to hide debug info
	- if there are any permissions requested by the app itself, they can probably be found here

### How to launch a local test
- In Terminal, navigate to the trendsetters folder
	- If environment is not built:
		- create the environment "conda env create -f environment.yml"
			- this requires that anaconda is installed as well as python 3.11
- activate the environment "conda activate trendenv"
	- if otree not installed
		- install otree "pip3 install -U otree"
- TO TEST: "otree devserver"
- in browser, open http://localhost:8000/

### Known Errors
- once you have launched a session, going to the "report" tab of the overview page causes an unhandled error
	- From Sentry:
> UndefinedVariable
> otree.views.admin.AdminReport
> Cannot resolve the variable 'decisionlist' (line 4, in "decisionlist")
 	- Ignore for now, just don't use report tab

## Code Documentation
*This is a WIP, started 9/6/2023. I am at least the third person to have worked on this project, and documentation has been sparse up until this point. I am hoping this clears some things up.*

### Code flow overview
The main file is settings.py. This outlines each of the "games" within the experiment. They are the following: Complete, Circle, Star, Line, and Survey. The last is a test to just run through the survey section which is at the end of each real game.

In the settings.py file there is an outline of the flow of each game, which proceeds through sections. This is the actual flow of the survey. A typical flow is: consent -> understanding1 -> block 1 -> understanding 2... -> survey -> end

Block 1 and understanding 1 are unique, as they have slightly different flows from the rest of the survey (block 1 has different payoffs, and understanding 1 has a large attention check/understanding confirmation section). Blocks 2-6 and understanding 2-6 are basically identical.

### Images
For reference, these images are all hosted on imgur and used for all of the network images, e.g. in the overview section, but also in all of the payout notifications and understanding questions. **I DO NOT KNOW WHO IS HOSTING THIS** or what account, I assume there is an imgur account floating around somewhere that has all of these files, but I have been unable to find it. In case the account gets removed for inactivity I am backing everything up.

I made a backup of each image used. It is stored based on network and then whether it is used in the "block" series or the "understanding" series. I pulled from block 1 and understanding 1, since it seems like everything else is just copied off of that. In the html files themselves there appear to be sections, so I broke it down by that and then visually by subsection so there weren't too many images in one folder. Annoyingly they are now jumbled within each folder but since each secton is ~6 images max that isn't too bad.

## File Overview

### List of files/folders that I think are unrelated to the current project
*9/22/23: I put these games inside OTree Demo Code folder to get them out of the way. These are mainly OTree demos and might be useful as reference but are not used by the experiment.*
- volunteer_dilemma
- trust_simple
- trust
- prisoner
- public_goods_simple
- matching pennies
- dictator
- cournot
- common value auction
- bertrand
- bargaining
- guess_two_thirds
- traveler_dilemma

### List of files/folders that *might* be unrelated
*proposed: don't touch!*
- templates
- templatestags
- static
- otreeutils
- admin_extensions
- Procfile
- \_rooms
- payment_info

### Files/Folders that are likely used but I don't understand
*proposed: work through these files and sort them into the other categories*
- \_builtin
- \_static
- \_templates
- Heroku | Invoice.pdf

### Files/Folders that are definitely used
*Don't touch! This doesn't include files that are generated during the running of the program, those are in the .gitignore*
- survey
- end
- consent
- circle* (aka anything that starts with "circle")
- line*
- star*
- complete*
- scripts.py
- settings.py

### Other
- LICENSE
- requirements.txt

## Old Notes

### Deployment Instructions - old

- Install Anaconda for dependency management
- Install oTree
- Create environment.yml file
	- name: trend
	- dependencies:
		- python=3.11.2
- Activate environment with common: conda activate trend
- Edit the code as you wish.
- Test code with otree devserver
- When ready call otree zip to zip the files.
- Upload to Otreehub in the trendsetters project.
	- *Note to self, where does Heroku come into play?*
	- *Second note, this could also be deployed from Github, but I assume that process is more complicated*
- Reset the database
- You’ll have to regenerate the links if you reset the database