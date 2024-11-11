# cite165-class-exercises
Contains the files needed for class exercises used in CITE 165 Linux System Administration taught in Fall 2024 semester at North Idaho College.

# Scenario Description

There is a cereal killer loose in [Insert City Name]. The police department have been working diligently to catch him and have managed to find his local hideout. They’ve done a search of the place and turned up his laptop.​

Your job is to gather information off his laptop to find out where he is going to strike next within 30 minutes.​

Forensics has told you there is a file (somewhere) on his computer that contains his passwords. The name of the file is likely "important_passwords", based off clues found in his hideout.​

# Instructions for Students

- Clone repository onto Linux system
    - `git clone https://github.com/jlreedNIC/cite165-class-exercises.git`
- Navigate into directory and set up files
    - `cd cite165-class-exercises`
    - `sudo ./execute_me.sh`

# For Instructors

No permanent changes are made to the Linux system (so far). The `execute_me.sh` script and associated files creates a 'trail' for students to be involved with the scenario. Running the script the first time will create files, make changes as necessary. Running the script again will undo those changes.

There is a submit program (`submit.py`) where students can submit their guesses after they think they've found all pieces of information. This file can be moved outside of the git repository directory, to make it easier for students to find and run. In order to see their guesses, the `listener.py` script will also need to be running. This program utilizes a free MQTT server. It is recommended to create your own MQTT server and change the information for your personal use. [HiveMQ](hivemq.com) was used.

## Trail of Bread Crumbs

- User is added to simulate 'cereal killer'.
    - username: cerealk
    - password: C3r3alK1ll3r (not encrypted)
    - user's name: Timothy Lybeck (thanks Tim for volunteering!)
    - A home directory is also created for this user, as well as a Trash and Documents directory.
- A fake 1099-MISC is moved into the Documents directory.
    - Shows address of the 'cereal killer' and who paid him (aka the ringleader).
- A .csv file containing commonly used passwords is moved into `/tmp/` directory.
    - Contains information needed to ssh into a remote server (aka the next place to be attacked).
    - This will require a `find` command to find.
- An entry to the `/etc/hosts` file is created, to create an alias for the server.
- A backup file is moved into the user Trash folder.
    - Contains personal address, and plans for world domination.
    - This is mostly just fun documents, and a way to practice the `tar` and `gzip` commands.
- The script will attempt to ssh into the server and fail to try to simulate failed authentication attempts.
