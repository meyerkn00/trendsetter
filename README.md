# Trendsetter Project

## Overview
Participants coordinate with three others (groups of 4) to solve a graph coloring problem.
- This means each round they select a color and get a payoff based on their selection and the decisions of others.
- The idea is they have to figure out how to coordinate on the best color.

There are four types of networks. Complete, circle, star, and line. Each network has a different level of visibility, meaning that participants can only see the decisions of a different number of group members.


There are 6 blocks of 10 rounds. 

In the first block, participants are led to select green, which results in a payoff of 12. All other selectios result in a payoff of 0.

In the second block, the participants are given the opportunity to earn more than 12. This is the key part of the experiment: *they are induced into a suboptimal equilibrium and then given the opportunity to get to the optimal equilibrium*

### Dependencies

**See requirements.txt**

- OTree
- Python 3.11.2
	- Use Anaconda for dependency management

### Deployment Instructions

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

## Code Documentation
*This is a WIP, started 9/6/2023*

### List of files/folders that I think are unrelated to the current project
*proposed solution: leave as-is for now but in the future put into an examples folder so they don't clog up the main folder*
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

### Files/Folders that are likely used but I don't understand
*proposed: either look into more or not, either way don't touch*
- \_builtin
- \_rooms
- \_static
- \_templates
- payment_info
- Heroku | Invoice.pdf

### Files/Folders that are definitely used
*Don't touch!*
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