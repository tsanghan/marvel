#!/usr/bin/env bash

export TS=$(date --utc +%s)
export HASH=$(echo -n $TS$PRI_KEY$PUB_KEY | md5sum | cut -d ' ' -f 1)
curl -s "https://gateway.marvel.com/v1/public/characters?ts=$TS&apikey=$PUB_KEY&hash=$HASH&name=Hulk" | jq -Mr '.'
