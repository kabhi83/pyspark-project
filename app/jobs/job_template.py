import pyspark.sql.functions as F
from pyspark.sql import DataFrame


def _extract_data(spark, config):
    """ Load data from csv file """


def _transform_data(raw_df):
    """ Transform raw dataframe """


def _load_data(config, transformed_df):
    """ Save/persist the data to a file or storage """


def run_job(spark, config):
    """ Run the job """
    _load_data(config, _transform_data(_extract_data(spark, config)))
