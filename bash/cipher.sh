#!/bin/bash

echo "Give me a password: "
read cipher

echo "Give password to unlock cipher: "
read pass

if [[ pass -eq cipher ]]; then
    echo "Unlocked"
else
    echo "Failed to unlock"
fi

