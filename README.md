# Readme
This is a simple script that pulls DFES information in our area. This was created after seeing some people
in our area badmouth the response time of our local volunteer firefighters. Just made for fun / to learn, but 
may be useful.

You will need to use pip3 to install the feeparser file

__pip3 install feedparser__

To run the file:

__python3 PullDFESInformation.py__

# TODO

- Create menu where users can choose from all areas
- Change pull* Functions to only append valid data to the array

# Change Log

## Version 1:
Version 1 is now completed. The application will check if there are any items from the feeds
and will only add them to the array if there are items that match the right parameters.
The application will also timeout if the information is not pulled from the site within 5 seconds (if the connection is made, and takes longer,it won't time out)