#!/bin/bash
function move {
    #Arguments for function move
    echo "Starting"
    local src="$1"
    local dst="$2"

    #Checking that src and dst directory exists
    if [ ! -d $src ]; then
        echo "The src directory does not exists."
        echo "Finish"
        exit 1
    fi

    if [ ! -d $dst ]; then
        echo "The dst directory does not exists"
        echo "Do you want to make a dst directory? Press yes or no"
        read answar
        if [ "$answar" == "no" ]; then
          echo "Finish"
          exit 1
        else
          mkdir $2
        fi
    fi

    if [ "$#" != 2 ]; then
      echo "Please enter correct argument, moving_From ---> moving_to"
      echo "Finish"
      exit 1
    fi

    echo "moving from $src ..."
    echo "moving to $dst ..."
    #extra implementation of moving specific file
    for file_type in *.txt *.dat
    do
      mv $src/$file_type $dst
    done
    echo "Finish"
}
move "$1" "$2"
