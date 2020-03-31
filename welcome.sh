#!/bin/bash

figlet -w $(tput cols) -c "Z" | lolcat

COLUMNS=$(tput cols) 
title=$(date +'%x %T')
printf "%*s\n" $(((${#title}+$COLUMNS)/2)) "$title" | lolcat
