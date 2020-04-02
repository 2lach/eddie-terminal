# How to setup Eddie the terminal greeter

```sh
python3 path-to-main-file path-to-quote username
#   1        2           3       4
```

|----------------------------------------------------------|
   Let's break these 4 arguments down
|----------------------------------------------------------|

1) python3 - the 3 is important cause even if sys default is py3 without the 3 it will be call by py2 from shell

2) /Users/stefan.lachmann/Desktop/Code/Forks/eddie/randline.py - this is the path from users to the main file, so it will run without errors no matter where in the pwd you are

3) /Users/stefan.lachmann/Desktop/Code/Forks/eddie/greetings.txt  - same as above but this file contains eddies quotes

4) Z - How you want eddie to adress

"""

**An example**
python3 /Users/stefan.lachmann/Desktop/Code/Forks/eddie/randline.py  /Users/stefan.lachmann/Desktop/Code/Forks/eddie/greetings.txt Z
