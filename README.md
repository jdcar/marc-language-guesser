# MARC record language guesser
This program uses the text in specific MARC tags to guess the language of the work so the fixed fields for language can be added programatically. The program is not 100% accurate so reviewing results is recommended. 

# Instructions

* Install packages
* The record set I started with included only records missing the fixed field for language of work
* I would recommend changing the 740 to another tag (if available, a tag that includes text that would help the program guess language) or removing from the code since most MARC records do not have this field.
* Change the filepath to your system
* I added the PyEnchant install : https://pypi.org/project/pyenchant/ . This is needed for the program to work with < 20 characters.
* This program only builds a new 008 tag. I use MARCedit to merge the new 008 tags into the original records
* In our system the unique bibliographic identifier is the 001 (mmsid). If your system is something other than Alma you will need to change this. Unless your system also puts the unique id in the 001!

# Other notes...

* This program includes a Python dictionary that converts fixed field codes from the two character ISO codes (639-1) to three character MARC codes (639-2). This is necessary because language_guesser uses the two character code.

# Credit to
https://pypi.org/project/guess_language-spirit/
https://pypi.org/project/pyenchant/ 
https://pypi.org/project/pymarc/ 