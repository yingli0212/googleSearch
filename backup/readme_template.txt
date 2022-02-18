# Googlesearch
## Introduction - This is a web service to be used by search keyword on google website.
### Summary - As results, the first ten results from google are shown. The search results is saved in a json file as output. You can find this json file in your current local directory.
### Features - 
## Requirements - Python 3.8
## Configuration - 
## Installation - 
## Usage - This web service is used via cURL. 
	 - Authentication uses the „username“ and a „verifycode“. 
	 - To each user an individual QRcode is generated during registration. This QRcode needs to be saved by user carefully. 
	 - User uses „Google Authenticator“ (An application in Appstore) to scann his QRcode to get a „Time base One Time Password“, namely verifycode. This verify code is changed all 30 seconds in „Google Authenticator“. This verifycode needs to be read out and given in the next step.
	 - In Command Line the following command needs to be given: curl "http://localhost:5000/search?username=youruser&verifycode=yourverifycode&keyword=yourkeyword“ > result.json
## Development - 
## Changelog - 
## FAQ - 
## Support - 
### Dos - 
### Contact - zhaoyingli1@hotmail.com