@echo off
REM connect-to-atlas.bat
REM Replace cluster0.xxxxx and <username> with the values from Atlas > Connect > Shell.
REM mongosh will ask for the password (safer than typing it in the command).

mongosh "mongodb+srv://cluster0.xxxxx.mongodb.net/" --apiVersion 1 --username <username>

REM Alternative: keep the full URI in an environment variable (set it once per terminal)
REM   set MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/
REM   mongosh "%MONGODB_URI%"
