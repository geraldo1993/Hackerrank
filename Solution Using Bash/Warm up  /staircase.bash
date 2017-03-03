#!/bin/bash

 read n;

  for((i=1;i<=n;i++))
  do

      for((k=i;k<=n-1;k++))
      do
        echo -ne " ";
      done

      for((j=0;j<=i-1;j++))
      do
	echo -ne "#"
      done

      echo;
  done
