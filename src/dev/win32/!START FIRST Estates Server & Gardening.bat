@echo off
title TTCY MongoDB

cd ../../../

:main
"src/dependencies/MongoDB\Server\3.0\bin\mongod.exe" --dbpath src/dependencies/MongoDB/GardeningDatabase


pause
