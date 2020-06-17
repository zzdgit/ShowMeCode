kinit -kt /home/datascience/datascience.keytab datascience
export PYSPARK_PYTHON=/home/datascience/anaconda3/bin/python
export PYTHONHASHSEED=0
export SPARK_YARN_USER_ENV=PYTHONHASHSEED=0
spark2-submit \
 --master yarn-client \
 --driver-memory 4G \
 --executor-memory 25G \
 --executor-cores 3 \
 --num-executors 10 \
 --queue root.datascience \
k_means.py

