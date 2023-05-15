import utils


class MapReduce(object):
    """
    MapReduce prototype model implemented in python

    Note: the 'mapper' and 'reducer' methods must be implemented to use the mapreduce model.
    """

    def __init__(self, input_dir=utils.default_input_dir, output_dir=utils.default_output_dir,
                 n_mappers=utils.default_n_mappers, n_reducers=utils.default_n_reducers,
                 clean=True):
        """
        :param input_dir: directory of the input files, taken from the default utils if not provided
        :param output_dir: directory of the output files, taken from the default utils if not provided
        :param n_mappers: number of mapper threads to use, taken from the default utils if not provided
        :param n_reducers: number of reducer threads to use, taken from the default utils if not provided
        :param clean: optional, if True temporary files are deleted, True by default.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.n_mappers = n_mappers
        self.n_reducers = n_reducers
        self.clean = clean

    def mapper(self, key, value):
        """
        Outputs a list of key-value pairs.

        Note: this function is to be implemented.
        """
        pass

    def reducer(self, key, values_list):
        """
        Outputs a single value together with the provided key.

        Note: this function is to be implemented.
        """
        pass