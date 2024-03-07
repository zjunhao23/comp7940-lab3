

import configparser

# Create an instance of ConfigParser
config = configparser.ConfigParser()

# Read the 'config.ini' file
config.read('config.ini')

# Access the 'ACCESS_TOKEN' value under the 'TELEGRAM' section
access_token = config['TELEGRAM']['ACCESS_TOKEN']

# Print the access token
print(access_token)
