import numpy as np
import pandas as pd

import wmfdata as wmf

def assert_tsv_loaded_correctly(file, table):
    """
    Checks that a loaded Data Lake table matches its source TSV file
    by comparing their Pandas representations.
    
    :param file: the file path of the source TSV
    :param table: The full name (database.table) of the loaded table 
    :returns: None, if the two datasets match
    :raises AssertionError: if the two datasets do not match
    """
    
    # To-do: check that `table` is a valid SQL identifier. Not a security issue,
    # but it's a good habit and theoretically makes for clearer error messages.

    source = pd.read_csv(
        file, 
        sep="\t",
        # By default, Pandas will parse strings like "nan" (language code for 
        # Southern Min) and "NA" (country code for Namibia) as nulls. This
        # prevents Pandas from interpreting *any* value as null.
        keep_default_na = False,
        # We still want to be able to represent nulls in the TSV. By default, 
        # Pandas writes nulls as empty fields, so we ask Pandas to interpret
        # empty strings (and nothing else) as nulls.
        na_values = [""]
    )
    
    loaded = wmf.presto.run(
        f"""
        SELECT *
        FROM {table}
        """
    )
    
    # Sort the data frames using the same method so that order
    # doesn't affect the results
    def sort(df):
        return df.sort_values(
            df.columns.to_list(),
            # We know the indexes have no information because we didn't
            # set one after reading
            ignore_index=True
        )
        
    source = sort(source)
    loaded = sort(loaded)

    # Hive loads empty strings as empty strings rather than nulls.
    # We need to improve our loading process to address this (T355847).
    # For now, prevent it from causing this test to fail.
    loaded = loaded.replace("", np.NaN)

    pd.testing.assert_frame_equal(
        source,
        loaded
    )
