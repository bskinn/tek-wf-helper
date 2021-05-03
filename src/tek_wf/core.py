r"""``tek_wf`` *core module*.

Helpers for streamlined work with oscilloscope traces recorded
by the Tektronix TBS-series and similar instruments

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    3 May 2021

**Copyright**
    \(c) Brian Skinn 2021

**Source Repository**
    https://github.com/bskinn/tek-wf-helper

**Documentation**
    *pending*

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""


import csv
import io
import re
from pathlib import Path

import attr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.integrate as spint
import scipy.optimize as spop


P_CSV_FNAME = re.compile(r"^F(\d+)CH(\d).CSV$", re.I)

COL_TIME = "Time"
COL_SIGNAL = "Signal"


def first_true(arr) -> int:
    return np.nonzero(arr)[0][0]


@attr.s(eq=False)
class ScopeTrace:
    path: Path = attr.ib(converter=Path)

    def __attrs_post_init__(self):
        self.csvdata: str = self.path.read_text()

        reader = csv.reader(io.StringIO(self.csvdata))
        self.data: np.ndarray = np.asarray(
            [[row[3], row[4]] for row in reader], dtype=float
        )
        self.df_data: pd.DataFrame = pd.DataFrame(
            self.data, columns=[COL_TIME, COL_SIGNAL]
        )

    def __getitem__(self, key):
        return self.df_data[key]

    def plot(self):
        plt.plot(self[COL_TIME], self[COL_SIGNAL])

    @property
    def time(self):
        return self[COL_TIME]

    @property
    def signal(self):
        return self[COL_SIGNAL]

    def time_between_times(self, *, start=None, end=None):
        result = self.time.copy()
        if start is not None:
            result = result.where(self.time >= start)
        if end is not None:
            result = result.where(self.time <= end)

        return result

    def signal_between_times(self, *, start=None, end=None):
        result = self.signal.copy()
        if start is not None:
            result = result.where(self.time >= start)
        if end is not None:
            result = result.where(self.time <= end)

        return result

    def time_between_signals(self, *, bottom=None, top=None):
        result = self.time.copy()
        if bottom is not None:
            result = result.where(self.signal >= bottom)
        if top is not None:
            result = result.where(self.signal <= top)

        return result

    def signal_between_signals(self, *, bottom=None, top=None):
        result = self.signal.copy()
        if bottom is not None:
            result = result.where(self.signal >= bottom)
        if top is not None:
            result = result.where(self.signal <= top)

        return result


@attr.s(eq=False)
class PairedTraces:
    folder: Path = attr.ib(converter=Path)

    def __attrs_post_init__(self):
        for pth in self.folder.iterdir():
            if mch := P_CSV_FNAME.match(pth.name):
                if mch.group(2) == "1":
                    self.ch1: ScopeTrace = ScopeTrace(pth)
                elif mch.group(2) == "2":
                    self.ch2: ScopeTrace = ScopeTrace(pth)

    def plot(self):
        self.ch1.plot()
        self.ch2.plot()
