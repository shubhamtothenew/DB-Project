# DB-Project
This project read the csv and makes a imported table and after that migrate this imported_table to a new migrated_table.

Requirements:

 1) python3.6
 
 2) tkinter- (sudo apt-get install python3-tk) 
 
 commands for running the script:
 1) For Import:
    python3.6 main.py -option import -to [import_tablename]
    
 2) For Migration:
    python3.6 main.py -option -from [import_tablename] -to [migtrate_tablename]   
