#!/bin/bash

PATH=$1

#set -e

if [[ -f $PATH ]]; then
	echo "$PATH exists!"
	echo "">> $PATH
        echo "You can edit $PATH"
else
	echo "You cannot edit $PATH"
fi
