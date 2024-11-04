#!/bin/bash

# check if user exists
username="cerealk"
passwordFileName="important_passwords.csv"
# head -n -1 foo.txt > temp.txt ; mv temp.txt foo.txt


if id "$username" >/dev/null 2>&1; then
    # delete files
    echo 'Scenario complete. Cleaning up files...'

    # remove username
    userdel -r $username
    # remove hidden password file
    mv /tmp/$passwordFileName ./.hidden/
    # remove line from host name
    head -n -1 /etc/hosts > /etc/temphosts; mv /etc/temphosts /etc/hosts
    echo "File clean up complete!"
else
    # create files
    echo 'Initializing files for scenario...'
    echo '...'

    # create user
    useradd -c "Timothy Lybeck" -d /home/cerealk/ -m -p "C3r3alK1ll3r" cerealk
    # create hidden password file
    mv ./.hidden/$passwordFileName /tmp/
    # create host name addition
    echo "74.179.83.108 ck-anon" >> /etc/hosts

    echo "Scenario ready!"
    
fi

