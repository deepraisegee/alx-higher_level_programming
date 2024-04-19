#!/bin/bash

if [ $# -eq 0 ]; then
    echo "No argument provided";
elif [ $# -gt 0 ]; then
    for i in $(ls); do
        if [ -f $i ]; then
            echo $i
        else
            echo "Not a file";
        fi
    done
fi
