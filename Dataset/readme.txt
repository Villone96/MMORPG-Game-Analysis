Travian Network Datasets
Contact: Alireza Hajibagheri, University of Central Florida (nima.hajibagheri@gmail.com)
-------------------------------------------------------------------------------
The files are bunded into RAR archives; each file represents one time slice of the network.

Reference:
If you want to use the network data please cite the following paper:
"Conflict and Communication in Massively-Multiplayer Online Games" 
Alireza Hajibagheri, Kiran Lakkaraju, Gita Sukthankar, Rolf T. Wigand, and Nitin Agrawal. 
Proceedings of the International Conference on Social Computing, Behavioral-Cultural Modeling, and Prediction. 2015. 

or our book chapter:
"Using Massively Multiplayer Online Game Data to Analyze the Dynamics of Social Interactions"
Alireza Hajibagheri, Gita Sukthankar, Kiran Lakkaraju, Hamidreza Alvari, Rolf T. Wigand, and Nitin Agrawal.
Social Interaction in Virtual Worlds, Cambridge University Press, 2017.


-------------------------------------------------------------------------------
CSV Files
Each line of the csv file consists of the following information:
uid1
User id for the first user (attacker, sender of the message, one of the traders)
uid2
User id for the second user (defender, receiver of the message, one of the traders)
-------------------------------------------------------------------------------
Graphml Files
Files with ".graphml" extension have the following features for every network node:
label
in-degree
out-degree

and edges:
label
time (in Linux format)
You can use network analysis packages in order to use these files. Also, most programming languages have packages available for reading graphml files and converting them into Graph and Network data structures.
-------------------------------------------------------------------------------
Community Membership

These are stored in txt files one for each day of the 30days period. Each line of the files contains a list of the uids that belong to the community at that timestep.
Lines with only one uid indicate communities of size one. Structure of communities changes over time.
