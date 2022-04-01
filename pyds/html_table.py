from .is_a_matrix import *
from .is_a_pandas_dataframe import *
from .make_key import *
from bs4 import BeautifulSoup
from pandas import DataFrame
import json
import os
import re


class HTMLTable:
    def __init__(self, x):
        assert isAMatrix(x), "`x` must be a matrix!"

        if not isAPandasDataFrame(x):
            x = DataFrame(x)

        self.data = x
        self.path = None

    def show(self, openCommand="firefox --private $FILE"):
        if self.path is None:
            self.path = os.path.realpath(makeKey(8) + ".html")
            self.save(self.path)
            print("Saved HTML file to: " + self.path)

        os.system(openCommand.replace("$FILE", self.path))
        return self

    def toString(self):
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

        out = regularTemplate.replace("{{ columns }}", columns).replace(
            "{{ rows }}", rows
        )
        soup = BeautifulSoup(out, "html5lib")
        return soup.prettify()

    def print(self):
        print(self.toString())
        return self

    def save(
        self, filename, shouldUseFancyTemplate=True,
    ):
        path = os.path.realpath(filename)
        tableString = self.toString()

        if shouldUseFancyTemplate:
            df = {
                "columns": self.data.columns.tolist(),
                "index": self.data.index.tolist(),
                "values": self.data.values.tolist(),
            }

            out = fancyTemplate.replace(
                "dataframe: null", "dataframe: " + json.dumps(df)
            )

        else:
            out = tableString

        with open(path, "w") as file:
            soup = BeautifulSoup(out, "html5lib")
            file.write(soup.prettify())

        self.path = path
        return self


selfPath = os.path.dirname(os.path.realpath(__file__))
fancyTemplatePath = os.path.join(selfPath, "html_table_fancy_template.html")
regularTemplatePath = os.path.join(selfPath, "html_table_template.html")

with open(fancyTemplatePath, "r") as file:
    fancyTemplate = file.read()

with open(regularTemplatePath, "r") as file:
    regularTemplate = file.read()
