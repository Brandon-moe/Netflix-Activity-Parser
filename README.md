# Netflix-Activity-Parser
Parses a Netflix Viewing Activity file and condenses it into a more accessible format.  
The activity file provided by Netflix lists all instances of show watching on your account, so it will contain 1000s of lines for any decently active account. It also contains the data for all profiles on the account.  
This tool condenses the file by grouping all the entries by series and only keeping the most recent episode you watched, so you can easily see where to pick up from if you've migrated to another media source which doesn't have your activity stored.  
The tool also allows you to pass a username as an argument, filtering the data to only contain entries for that account.

# Installation and Usage 
The tool uses Python 3 with the Pandas library. You can download Python from the following link: https://www.python.org/downloads/  
Once installed, you can install pandas with the command `pip install pandas` or `pip install requirements.txt`  
The tool will look for your activity file in the same directory as the project.  
Run the tool with `python main.py <username>` and an output file will be produced with the condensed data.  

