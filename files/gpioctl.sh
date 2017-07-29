#!/bin/bash

if [ "$#" -ne 2 ]
then
    echo "Usage: command name value"
    exit 1
fi

echo $1,$2 > /etc/mistlogic/gpio.fifo
