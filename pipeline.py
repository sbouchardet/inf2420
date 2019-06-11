class Pipeline:
    def __init__(self, pipeline_name):
        self.__name = pipeline_name
        self.__functions = []
        self.__results = []

    def add_function(self, func):
        self.__functions.append(func)

    def run(self, *args):
        for f in self.__functions:
            self.__results.append(f(*args))

    def show_results(self):
        for func_result in  zip(self.__functions, self.__results):
            func = func_result[0]
            result = func_result[1]
            print("{} = {}".format(func,result))
