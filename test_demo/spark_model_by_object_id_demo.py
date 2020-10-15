__author__ = 'reneiw'
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
from sklearn.ensemble import IsolationForest
import numpy as np

import pandas as pd
from datetime import datetime


def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def partition_func(rows):
    rows = [row.asDict() for row in rows]
    if len(rows) == 0:
        return []
    abnormal_df_ = pd.DataFrame(rows)
    fault_df_ = fault_data.value
    wells = abnormal_df_.dxmc.unique()
    for well in wells:
        abnormal_df = abnormal_df_[abnormal_df_.dxmc == well].sort_values(by='cjsj')
        fault_df = fault_df_[fault_df_.well_name == well]
        abnormal_feature = get_abnormal_feature(abnormal_df, fault_df)
        for f in abnormal_feature:
            yield [f]


def get_abnormal_feature(abnormal_df, fault_df):
    m1 = IsolationForest(contamination=0.05)
    np.random.seed(336)
    m1.fit(abnormal_df[features])
    important_features = 0
    for m in m1.estimators_:
        important_features += m.feature_importances_
    important_features = pd.Series(important_features, index=features).sort_values(ascending=False)
    important_features = important_features.iloc[:21].index.values

    abnormal_features = []
    for _, row in fault_df.iterrows():
        start_time = row['start_time']
        end_time = row['end_time'] + ' 23:59:59'
        outlier_df = abnormal_df[(abnormal_df.cjsj >= start_time) & (abnormal_df.cjsj <= end_time)
                                 & (abnormal_df.iso_outlier == -1)]
        normal_df = abnormal_df[(abnormal_df.cjsj < start_time) & (abnormal_df.iso_outlier == 1)]
        normal_df = normal_df.iloc[-outlier_df.shape[0] * 2:]
        outlier_mean, outlier_std = outlier_df[important_features].mean(), \
            outlier_df[important_features].std()
        normal_mean, normal_std = normal_df[important_features].mean(), \
            normal_df[important_features].std()
        z_score = (outlier_mean - normal_mean) / normal_std
        res = list(zip(important_features, normal_mean.astype(str), outlier_mean.astype(str), z_score.astype(str),
                       normal_std.astype(str), outlier_std.astype(str)))
        res = '\t'.join(['\t'.join(r) for r in res])
        abnormal_features.append('\t'.join(row.astype(str).values.tolist()) + '\t' + res)
    return abnormal_features


if __name__ == "__main__":
    sparkConf = SparkConf()
    sparkConf.setAppName("dagang abnormal segment")
    sparkConf.set("spark.kryoserializer.buffer.max", "128")
    sc = SparkContext(conf=sparkConf)
    sc.setLogLevel("WARN")
    sqlCtx = HiveContext(sc)
    sqlCtx.setConf("spark.sql.parquet.binaryAsString", "true")
    sqlCtx.setConf("spark.sql.hive.convertMetastoreParquet", "true")
    sqlCtx.setConf("spark.sql.parquet.int96AsTimestamp", "true")

    executor_cores = int(sparkConf.get('spark.executor.cores'))
    num_executors = int(sparkConf.get('spark.executor.instances'))
    num_partitions = executor_cores * num_executors * 3

    features = ['area', 'down_oscillation', 'down_stroke', 'down_stroke_ratio', 'down_stroke_zaihe',
                'down_up_oscillation_ratio', 'down_up_stroke_zaihe_ratio',
                'down_up_zaihe_ratio', 'down_zaihe', 'left_upper_area', 'left_upper_area_ratio',
                'max_weiyi', 'max_weiyi_zaihe',
                'max_zaihe', 'min_max_zaihe_ratio', 'min_weiyi', 'min_weiyi_zaihe',
                'min_zaihe', 'up_oscillation', 'up_stroke',
                'up_stroke_ratio', 'up_stroke_zaihe', 'up_zaihe']

    print(current_timestamp(), '-' * 30 + 'starting')
    abnormal_sql = """
        select * from industry.dagang_abnormal
        where dwdm like '03%'
    """
    fault_sql = """
        select * from industry.fault_segment_2c
    """
    abnormal_data = sqlCtx.sql(abnormal_sql) \
        .repartition(num_partitions, 'dxmc').cache()
    fault_data = sc.broadcast(sqlCtx.sql(fault_sql).toPandas())

    print(current_timestamp(), '-' * 30 + 'spark learning_data rows count', abnormal_data.count())
    res_rdd = abnormal_data.rdd.mapPartitions(partition_func).cache()
    print(current_timestamp(), '-' * 30 + 'res_rdd rows count: ', res_rdd.count())
    res_df = sqlCtx.createDataFrame(res_rdd, schema=['res']).toPandas()
    res_df.to_csv('abnormal_feature.csv', index=False, header=None)
    print(current_timestamp(), '-' * 30 + 'finished')
