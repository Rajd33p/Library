## Feature
* Issuing
* Collection
* Stock Check
* Login Screen


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirement.

```bash
pip install -r requirements.txt 
```

## SQL schema

```sql
CREATE TABLE IF NOT EXISTS `books` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Author` varchar(30) NOT NULL,
  `Genre` varchar(50) DEFAULT NULL,
  `Quantity` int(11) NOT NULL,
  `Issused` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `issued` (
  `Name` varchar(30) NOT NULL,
  `ID` int(5) NOT NULL DEFAULT 0,
  `Add_no` int(11) NOT NULL,
  `Book_ID` int(11) NOT NULL,
  `Iss_D` date NOT NULL,
  `Status` varchar(10) NOT NULL,
  `Rcv_D` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


```
## Update Database settings in features.py
```python

mydb = mysql.connector.connect(
    host="HOST",
    user="USERNAME",
    passwd="PASSWORD",
    database="DB NAME"
)
   
```
## Todo
* Write a cleaner and more elaborate Readme.md 
* Clean code and make it more human readable 
* Make a config.py file 
