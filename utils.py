# set default directory for the input files
default_input_dir = "input_files"
# set default directory for the output files
default_output_dir = "output_files"
# set default directory for the temporary map files
default_map_dir = "temp_map_files"

# set default number for the map and reduce threads
default_n_mappers = 4
default_n_reducers = 4


# return the name of the input file to be split into chunks
def get_input_file(input_dir=None, extension=".csv"):
    if not (input_dir is None):
        return input_dir + "/data" + extension
    return default_input_dir + "/data" + extension


# return the name of the current split file corresponding to the given index
def get_input_split_file(index, input_dir=None, extension=".csv"):
    if not (input_dir is None):
        return input_dir + "/data_" + str(index) + extension
    return default_input_dir + "/data_" + str(index) + extension


# return the name of the temporary map file corresponding to the given index
def get_temp_map_file(index, reducer, output_dir=None, extension=".csv"):
    if not (output_dir is None):
        return output_dir + "/map_data_" + str(index) + "-" + str(reducer) + extension
    return default_output_dir + "/map_data_" + str(index) + "-" + str(reducer) + extension


# return the name of the output file given its corresponding index
def get_output_file(index, output_dir=None, extension=".out"):
    if not (output_dir is None):
        return output_dir + "/reduce_data_" + str(index) + extension
    return default_output_dir + "/reduce_data_" + str(index) + extension


# return the name of the output file
def get_output_join_file(output_dir=None, extension=".out"):
    if not (output_dir is None):
        return output_dir + "/output" + extension
    return default_output_dir + "/output" + extension
