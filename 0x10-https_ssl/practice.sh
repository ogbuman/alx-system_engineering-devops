#!/bin/bash

add ()
{
  if [[ -z $1 ]]
  then
    echo "No arg passed"
  else
    echo $(("$1"+"$2"))
  fi
}

add "$1" "$2"
