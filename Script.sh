# Script to extract tweets and save to hdfs for spark processing
./Twit_load.py
jps
start-dfs.sh
start-yarn.sh
jps
hadoop fs -mkdir /sparkuser
hadoop fs -put ./Tweets_*.* /sparkuser
hadoop fs -ls /sparkuser/
