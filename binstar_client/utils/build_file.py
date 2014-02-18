'''
Created on Feb 18, 2014

@author: sean
'''


initial_build_config ='''
## The package attribure specifies a binstar package namespace to build the package to. 
## This can be specified here or on the command line
package: %(PACKAGE_NAME)s

## You can also specify the account to upload to,
## you must be an admin of that account, this 
## defaults to your user account
# user: USERNAME 

#===============================================================================
# Build Matrix Options
# Thes options may be a single item, a list or empty
# The resulting number of builds is [platform * engine * env] 
#===============================================================================

## The platforms to build on.
## platform defaults to linux-64 
# platform: 
#  - linux-64
#  - linux-32
## The engine are the inital conda packages you want to run with 
# engine:
#  - python=2
#  - python=3
## The env param is an environment variable list 
# engine:
#  - MY_ENV=A CC=gcc
#  - MY_ENV=B

#===============================================================================
# Scrip options
# Thes options may be broken out into the before_script, script and after_script
# or not, that is up to you 
#===============================================================================

## Run before the script
# before_script:
#   - echo "before_script!"
## Put your main computations here!  
script:
  - echo "This is my binstar build!"
## This will run after the script regardless of the result of script
## BINSTAR_BUILD_RESULT=[succcess|failure] 
# after_script:
#   - echo "The build was a $BINSTAR_BUILD_RESULT" | tee artifact1.txt
## This will be run only after a successfull build
# after_success:
#   - echo "after_success!"
## This will be run only after a build failure
# after_failure:
#   - echo "after_failure!"

#===============================================================================
# Build Results
# Build results are split into two categories: artifacts and targets
# You may omit either key and stiff have a successfull build
# They may be a string, list and contain any bash glob
#===============================================================================

## Build Artifacts: upload anything you want!
## Your build artifacts will be put into the website
## http://artifacts.build.binstar.info/USERNAME/PACKGE_NAME/BUILD_NO
## You can store all logs or any derived data here
## Remember, the site http://artifacts.build.binstar.info is NOT secure and does not
## require a user to log in to view
# build_artifacts:
#   - *.log

## Build Targets: Upload these files to your bunstar package
# build_targets:
#   - dist/*
'''