# Pre-requisites:

Python3


# Setup:

You will have to grant access to this script for sending emails from your inbox using this steps mentioned here: https://hotter.io/docs/email-accounts/secure-app-gmail/

After this is done, just edit the config part of script to set the pincode you want to search, age group and your email and password  and it will automatically serach slots and send an email in case slots are available.

The job will run everyday at 12:00 by default. You can modify that if you wish to.


# Execute:

pip install -r requirements.txt

nohup python get_slots_for_vaccination.py &
