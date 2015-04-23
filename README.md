# MapReduceMincemeat
Example of Lightweight MapReduce in python


### Getting Started
* Example from mincemeat example


Execute this script on the server:

```bash
python example.py
```

Run mincemeat.py as a worker on a client:

```bash
python mincemeat.py -p changeme [server address]
```
And the server will print out:

```python
{'a': 2, 'on': 1, 'great': 1, 'Humpty': 3, 'again': 1, 'wall': 1, 'Dumpty': 2, 'men': 1, 'had': 1, 'all': 1, 'together': 1, "King's": 2, 'horses': 1, 'All': 1, "Couldn't": 1, 'fall': 1, 'and': 1, 'the': 2, 'put': 1, 'sat': 1}
```

### Doing More

#### Math Stats
Math stats - mathstats.py -  Given a text file name on the command-line containing one number per line, print out the sum, count, and standard-deviation of all the numbers in the file.  All statistics should be found in one pass through the data.

```bash
python mathstats.py small.txt
python mathstats.py medium.txt
python mathstats.py large.txt
```


#### Letter Frequency
Letter Frequency - freq.py - Given a text file name on the command-line containing a text document, print out the number of times each character is used, along with the percent of the total with 2 decimal places.  Sort the output so the most seen character is on the bottom.

```bash
python freq.py smalldick.txt
python freq.py mobydick.txt
```


#### Password Cracking
Password cracking - passCrack.py - Given a string of characters on the command line, find what string hashes to it.  Passwords are sometimes stored in a hashed form, so if the database is breached, the passwords are not easily usable. For this assignment, assume we have a hash of a password in hex form.  Given this hash on the command line, find what password hashes to it.  Only the first 5 characters of the hash are checked.  Assume passwords are 4 or fewer characters containing only lowercase letters and numbers.  Use MapReduce to quickly look through all combinations for a match.  Print out the input hash string and the valid passwords which hash to it, if any.  Use hashlib md5 hexdigest()and use the first 5 characters.

```bash
python passCrack.py d077f
#this might take a good 15 minutes
# expected answer {'found': ['cat', 'gkf9']}

python passCrack.py 0832c
# expected answer {'found': ['cats', 'zb8e']}
```

I would sping multiple servers when running this command. 


