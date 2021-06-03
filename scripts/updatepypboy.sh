#!/bin/bash

cd ~/pypboy && git stash && git pull fetch --all && git checkout --force "origin/master" && chmod 777 main.py
