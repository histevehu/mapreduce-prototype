import sys
import utils
from mapreduce import MapReduce


class passenger_analysis(MapReduce):
    def __init__(self, input_dir, output_dir, n_mappers, n_reducers):
        MapReduce.__init__(self, input_dir, output_dir, n_mappers, n_reducers, True)

    def mapper(self, key, value):
        """
        The map function used to analyze the number of passenger flights.
        """
        results = []
        count = 1
        # seperate line into words
        value = [s for s in value.split('\n') if s]
        for v in value:
            results.append((v.split(',')[0], count))
        return results

    def reducer(self, key, values):
        """
        The reduce function used to analyze the number of passenger flights.
        """
        wordcount = sum(value for value in values)
        return key, wordcount


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("<i> Default arguments used:", utils.default_input_dir, utils.default_output_dir, utils.default_n_mappers,
              utils.default_n_reducers)
        input_dir, output_dir, n_mappers, n_reducers = utils.default_input_dir, utils.default_output_dir, utils.default_n_mappers, utils.default_n_reducers
    else:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        n_mappers = int(sys.argv[3])
        n_reducers = int(sys.argv[4])
    word_count = passenger_analysis(input_dir, output_dir, n_mappers, n_reducers)
    word_count.run()
    print("<i> Results stored in:", output_dir)
