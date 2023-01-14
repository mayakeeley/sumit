#!/bin/bash

#
# Creating sumit git repo
#
git init
git add .
git commit -m "Initial commit"
# git remote add origin git@github.com:thinknimble/sumit.git
gh repo create thinknimble/sumit --private -y
git push origin main
printf "\033[0;32mRepo https://github.com/thinknimble/sumit/\033[0m \n"
