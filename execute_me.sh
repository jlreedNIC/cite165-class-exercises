#!/bin/bash

# check if user exists
username="cerealk"
passwordFileName="important_passwords.csv"
backupFileDir="backup"


if id "$username" >/dev/null 2>&1; then
    # delete files
    echo 'Scenario complete. Cleaning up files...'

    # remove username
    userdel -rf $username
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
    useradd -c "Timothy Lybeck" -d /home/$username/ -m -p "C3r3alK1ll3r" cerealk
    # create trash folder if not there
    mkdir -p /home/$username/.local/share/Trash
    # create hidden password file
    mv ./.hidden/$passwordFileName /tmp/
    # create host name addition
    echo "74.179.83.108     74.179.83.108     Quaker-HQ" >> /etc/hosts
    # create backup files
    cd .hidden
    tar -cf $backupFileDir.tar $backupFileDir/
    gzip $backupFileDir.tar
    cd ..
    mv .hidden/$backupFileDir.tar.gz /home/$username/.local/share/Trash/
    # simulate failed authentication attempts
    ssh -o PasswordAuthentication=no -q itadmin@Quaker-HQ
    ssh -o PasswordAuthentication=no -q itadmin@Quaker-HQ
    ssh -o PasswordAuthentication=no -q itadmin@Quaker-HQ
    ssh -o PasswordAuthentication=no -q itadmin@Quaker-HQ
    ssh -o PasswordAuthentication=no -q itadmin@Quaker-HQ

    echo "Scenario ready!"
    
fi

