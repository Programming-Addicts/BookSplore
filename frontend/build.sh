#!/bin/bash

echo "Building"

npx vue-cli-service build

rm ../backend/dist -rf
cp dist ../backend/ -r
rm dist -rf

echo "Turn on Live Reload(Note: You should run the backend before selecting this)? [Yn]"
read input

if [[ $input = "n" ]]
then
	exit
else
	npx vue-cli-service build --dest "../backend/dist" --watch
fi