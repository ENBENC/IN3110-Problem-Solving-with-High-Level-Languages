#!/bin/bash
startTime=""
endTime=""
taskName=""
start_count=0
end_count=0
diffTime=""
log_output=""

#start the tracker by return the startTime
#The track_start require 1 parameter
function track_start {
  local started=$1
  if [ "${started}" = "" ]; then
    startTime=$(date +"%c")
    start_count=$(date +%s)
    echo "Starting the track at: $startTime"
  else
    echo "The task $taskName is running"
  fi

}
function secound_translator {
  diffTime+="Task$taskName:$(($1/3600)):$((($1%3600)/60)):$(($1%60))\n"
}

#if the tracker has started then return a string of ending endTime
#else then return a empty string
#The track_stop require 1 string parameter
function track_stop {
  local started=$1

  if [ "${started}" = "" ]; then
    echo "Please start the tracker first: : track start task_Name!"
    echo ""
  else
    endTime=$(date +"%c")
    echo "Ending the track at: $endTime"

    #Here we count the time this task spent
    end_count=$(date +%s)
    dt=`expr ${end_count} - ${start_count}`
    secound_translator dt

    log_maker
    startTime=""
    endTime=""
    taskName=""
    start_count=0
    end_count=0
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

function track_log {

  if [ $diffTime = "" ]; then
    echo "Please start the tracker first: track start task_Name!"
  else
    printf $diffTime
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
  elif [ "$1" = "log" ]; then
    track_log
  else
      echo "track start NAME - start the tracker"
      echo "track status - give status"
      echo "track stop - end the tracker"
      echo "track log - print log of time spent on each task"
      echo ""
  fi
}
