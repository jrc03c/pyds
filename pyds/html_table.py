import json
import os

from bs4 import BeautifulSoup
from pandas import DataFrame

from .is_a_matrix import is_a_matrix
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .make_key import make_key


class HTMLTable:
    def __init__(self, x):
        assert is_a_matrix(x), "`x` must be a matrix!"

        if not is_a_pandas_dataframe(x):
            x = DataFrame(x)

        self.data = x
        self.path = None

    def show(self, open_command='firefox --private "$FILE"'):
        if self.path is None:
            self.path = os.path.realpath(make_key(8) + ".html")
            self.save(self.path)
            print("Saved HTML file to: " + self.path)

        os.system(open_command.replace("$FILE", self.path))
        return self

    def to_string(self):
        columns = ""
        rows = ""

        for col in self.data.columns:
            columns += "<th>" + str(col) + "</th>"

        for i in range(0, self.data.shape[0]):
            row = self.data.values[i]
            index = self.data.index[i]
            rows += "<tr><td>" + str(index) + "</td>"

            for value in row:
                rows += "<td>" + str(value) + "</td>"

            rows += "</tr>"

        out = regular_template.replace("{{ columns }}", columns)
        out = out.replace("{{ rows }}", rows)
        soup = BeautifulSoup(out, "html5lib")
        return soup.prettify()

    def print(self):
        print(self.to_string())
        return self

    def save(
        self,
        filename,
        should_use_fancy_template=True,
    ):
        path = os.path.realpath(filename)

        if should_use_fancy_template:
            df = {
                "columns": self.data.columns.tolist(),
                "index": self.data.index.tolist(),
                "values": self.data.values.tolist(),
            }

            out = fancy_template.replace(
                "dataframe: null", "dataframe: " + json.dumps(df)
            )

        else:
            out = self.to_string()

        with open(path, "w") as file:
            soup = BeautifulSoup(out, "html5lib")
            file.write(soup.prettify())

        self.path = path
        return self


self_path = os.path.dirname(os.path.realpath(__file__))
fancy_template_path = os.path.join(self_path, "html_table_fancy_template.html")
regular_template_path = os.path.join(self_path, "html_table_template.html")

with open(fancy_template_path, "r") as file:
    fancy_template = file.read()

with open(regular_template_path, "r") as file:
    regular_template = file.read()
