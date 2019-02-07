import pandas as pd

# DEMONSTRATION OF CONVERSIONS BETWEEN JSON AND DATAFRAME

df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])
print("Original DataFrame:")
print(df)
# Original DataFrame:
#       col 1 col 2
# row 1     a     b
# row 2     c     d

# === split oriented

json_formatted_data = df.to_json(orient='split')
print("Split oriented, Formatted as JSON:")
print(json_formatted_data)
# '{"columns":["col 1","col 2"],
#   "index":["row 1","row 2"],
#   "data":[["a","b"],["c","d"]]}'

df2 = pd.read_json(json_formatted_data, orient='split')
assert df.equals(df2),  "convert and convert back failed for split type conversion"

# === index oriented

json_formatted_data = df.to_json(orient='index')
print("Index oriented, Formatted as JSON:")
print(json_formatted_data)
# {"row 1":{"col 1":"a","col 2":"b"},
#  "row 2":{"col 1":"c","col 2":"d"}}

df2 = pd.read_json(json_formatted_data, orient='index')
assert df.equals(df2),  "convert and convert back failed for split type conversion"

# === records oriented (index labels lost)

json_formatted_data = df.to_json(orient='records')
print("Index oriented, Formatted as JSON:")
print(json_formatted_data)
# '[{"col 1":"a","col 2":"b"},
#   {"col 1":"c","col 2":"d"}]'

df2 = pd.read_json(json_formatted_data, orient='records')
assert df.equals(df2),  "convert and convert back failed for split type conversion"

