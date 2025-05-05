#!/bin/sh
exec ./kissat --psids=true --target=1 --walkinitially=true --chrono=true $1 $2/proof.out
