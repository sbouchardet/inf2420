from dataset_manager import DatasetManager
from dataset_loader.data_source import DataSource
import pandas as pd
import zipfile
import urllib.request
import os

class DatasetLoader(object):

    def __init__(self, dataset_manager_path):
        self.__dm=DatasetManager(dataset_manager_path)
        self.datasources = self.__get_datasources_list(self.__dm)

    def __get_datasources_list(self, dataset_manager):
        dm_list = dataset_manager.list_datasets()
        datasources = {}
        #TODO: If the function `list_datasets` returns a list of dicts,
        # would be better to create the DataSources
        for dm in dm_list.to_dict(orient='records'):
            identifier = dm["identifier"]
            source = dm["source"]
            description = dm["description"]
            format = dm["format"]
            local_source = dm["local_source"]
            datasources[identifier] = DataSource(identifier, source, description, format, local_source)
        return datasources

    def download_all_data(self):
        for k in self.datasources:
            self.download_datasource(k)

    def download_datasource(self, identifier):
        datasource = self.datasources[identifier]
        datasource.download()

    def unzip_datasource(self, identifier):
        datasource = self.datasources[identifier]
        datasource.unzip_file()

    def unzip_all_data(self):
        for k in self.datasources:
            self.unzip_datasource(k)

    def load_as_pandas(self,identifier, *args, **kargs):
        return self.datasources[identifier].load_as_pandas()
