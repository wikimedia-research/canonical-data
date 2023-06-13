import argparse
import os

import wmfdata as wmf


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--database",
        help="Name of the database to put the table countres into",
        default="canonical_data",
    )
    parser.add_argument("--data_file", help="TSV table", default="countries.tsv")
    parser.add_argument(
        "--create_table_statement",
        help="TSV table",
        default="create_canonical_data_countries_table.hql",
    )
    args = parser.parse_args()

    spark = wmf.spark.get_session(type="local")

    cwd = os.getcwd()
    df = spark.read.csv(f"file:///{cwd}/{args.data_file}", header=True)
    print(f"Filling {args.database}.countries with {df.count()} line(s)")

    query = f"use {args.database};\n" + open(args.create_table_statement).read()
    print(query)
    spark.sql(query)

    df.write.mode("overwrite").saveAsTable(args.table)


if __name__ == "__main__":
    main()
