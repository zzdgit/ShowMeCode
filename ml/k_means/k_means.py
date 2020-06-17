import uuid
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

def get_data():
    seeds_dataset.to_csv('./seeds_dataset.csv', index=None)
    seeds_dataset.columns = ['area', 'perimeter', 'compactness', 'length_of_kernel',
                             'width_of_kernel', 'asymmetry_coefficient',
                             'length_of_groove', 'class']
    

def kmeans():
    spark = SparkSession \
        .builder \
        .appName('my_first_app_name') \
        .getOrCreate()
    df = spark.read.csv('./seeds_dataset.csv', header=True, inferSchema=True)
    df.show(5)

    assembler = VectorAssembler(inputCols=df.columns, outputCol='features')
    final_df = assembler.transform(df)
    final_df.show(3)
    final_df.take(1)

    # instantiated kmeans with 3 cluster
    kmeans = KMeans(k=3)
    # fitting the model
    model = kmeans.fit(final_df)
    centers = model.clusterCenters()
    print(centers)
    model.transform(final_df).select('prediction').show()

class SparkKMeans():
    def __init__(self):
        self.appname = uuid.uuid1()
        self.spark = SparkSession.builder.appName(self.appname).getOrCreate()

    def readdata(self, datapath):
        try:
            df = self.spark.read.csv(datapath, header=True, inferSchema=True)
            df.show(5)
            return df
        except Exception as e:
            raise e

    def train(self, df, k=2, maxIter=20):
        assembler = VectorAssembler(inputCols=df.columns, outputCol='features')
        final_df = assembler.transform(df)
        kmeans = KMeans(k=k, maxIter=maxIter)
        model = kmeans.fit(final_df)
        centers = model.clusterCenters()
        print(centers)
        model.transform(final_df).select('prediction').show()
        model.transform(final_df).show()
        data = model.transform(final_df)
        return data

if __name__ == "__main__":
    datapath = '/user/datascience/zhouzhengdong/seeds_dataset.csv'
    sk = SparkKMeans()
    df = sk.readdata(datapath)
    data = sk.train(df)
