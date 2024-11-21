# Monopoly (Group 32)

## Description

Built OS: Windows
IDE: PyCharm 2024.3
Suggested Python version: 3.12, 3.13
No external libraries required

## Setup

### To prepare the program

1. Using git clone command

```
gh repo clone chinghei1007/SE0911_3
```

2. Pycharm: get from VCS --> URL

``` 
https://github.com/chinghei1007/SE0911_3 
```

### Configuration and execute

1. Change ```[DEFAULT][path]``` inside ```config.ini``` to switch to desire property text file
2. Property file should be formatted as follows

    - Comma-separated, three items per line. For example
   ```
   {name}, {price}, {rent}
   ```
    - Always have **20** lines of property information
    - **Non-property** squares should have {price} and {rent} 0

        - Only one **Go** and **Jail** is allowed
        - Between one to three **Chance, Tax** and **Go To Jail** is allowed
        - **All special squares are case-sensitive**
3. To run the program, execute ```game.py```
4. In case the original ```property.txt ``` is corrupted, please copy the backup property list
   in ```\backup property\property.txt```
