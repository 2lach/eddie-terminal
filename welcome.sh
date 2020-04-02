#!/bin/bash

# In order to run this script lolcat & figlet must be installed (both are highly available for most systems)
    # lolcat > [original (ruby) https://github.com/busyloop/lolcat] (c) [https://github.com/jaseg/lolcat] 
    # figlet > [http://www.figlet.org/]

figlet -w $(tput cols) -c "Z" | lolcat

COLUMNS=$(tput cols) 
title=$(date +'%x %T')
printf "%*s\n" $(((${#title}+$COLUMNS)/2)) "$title" | lolcat
