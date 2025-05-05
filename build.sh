#!/bin/sh
cd kissat-sc2024
./configure --quiet
make all || exit 1
exec install -s build/kissat ../

