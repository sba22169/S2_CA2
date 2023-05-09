#!/bin/bash

# Script to extract tweets and save to hdfs for spark processing

python3 Twit_load.py
sleep 8m
jps
start-dfs.sh
sleep 8s

start-yarn.sh
sleep 8s

jps
sleep 20s
hadoop fs -mkdir /sparkuser
hadoop fs -put ./CA2_TWEETS_*.* /sparkuser
hadoop fs -ls /sparkuser/
