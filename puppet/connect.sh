#!/usr/bin/env bash

stage="127.0.0.1"
prod="127.0.0.1"

if [ $1 == "stage" ]; then
    ssh deploy@$stage
elif [ $1 == "prod" ]; then
    ssh deploy@$prod
fi
