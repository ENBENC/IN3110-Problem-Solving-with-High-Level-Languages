#!/bin/bash
startTime=""
endTime=""
taskName=""

#start the tracker by return the startTime
#The track_start require 1 parameter
function track_start {
  local started=$1
  if [ "${started}" = "" ]; then
    startTime=$(date +"%c")
    echo "Starting the track at: $startTime"
  else
    echo "The task $taskName is running"
  fi

}

#if the tracker has started then return a string of ending endTime
#else then return a empty string
#The track_stop require 1 string parameter
function track_stop {
  local started=$1
  endTime=$(date +"%c")

  if [ "${started}" = "" ]; then
    echo "Please start the tracker first: : track start task_Name!"
    echo ""
  else
    echo "Ending the track at: $endTime"
    log_maker
    startTime=""
    endTime=""
    taskName=""
  fi
}
#Takes no parameter
function log_maker {
  touch ~/.local/share/log.txt

  cat << EOF >> ~/.local/share/log.txt
START $startTime
LABEL This is task $taskName
END $endTime

EOF
}

#if the tracker has started then tell the user when and the name of task
#if the tracker dont have an active task, then tell the user to active it
#The track_status require 1 string parameter
function track_status {
  local started=$1

  if [ "${started}" = "" ]; then
    echo "Please start the tracker first: track start task_Name!"
  else
    echo "This is task: $taskName"
    echo "Started at: $startTime"
  fi
}

function track {
  LOGFILE="~/.local/share/log.txt"
  if [ "$1" = "start" ]; then
    taskName=$2
    track_start $startTime
  elif [ "$1" = "status" ]; then
    track_status $startTime
  elif [ "$1" = "stop" ]; then
    track_stop $startTime
  else
      echo "track start NAME - start the tracker"
      echo "track status - give status"
      echo "track stop - end the tracker"
      echo ""
  fi
}
