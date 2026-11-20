"""models.py – Lab 4: classes that describe the "things" in your data.

WHAT GOES HERE
    One class per real-world object of your topic. A class keeps the data of
    one object together with the operations on it (methods).
    Typically: a class for ONE record (one row) and a class that collects
    many records (e.g. a player with all his shots, a city with all its
    measurements).

EXAMPLE (reference project – basketball shots)
    shot = Shot.from_row(row)        shot.points -> 3, shot.is_three -> True
    curry = Player("Stephen Curry")  curry.add(shot); curry.fg_pct()
"""

# Your code from Lab 4 goes below.
from src.stats import count_by, group_stat
class Dataset:
    def __init__(self, rows, name="data"):
      self.rows = rows
      self.name = name

    def __len__(self):
        return len(self.rows) 

    def __str__(self):
        return f"Dataset '{self.name}': {len(self)} rows"


    def column(self, name):
        return [row[name] 
          for row in self.rows 
          if row[name] is not None]
        
    def where(self, column, value):
        chosen = [row for row in self.rows if row[column] == value]
        return Dataset(chosen, f"{self.name} | {column} = {value}")

    def count_by(self, key):
        return count_by(self.rows, key)

    def group_stat(self, group, value, how="mean"):
        return group_stat(self.rows, group, value, how)

class Analysis:

    def __init__(self, name):
        self.name = name                 # every analysis has a name (used in the report)

    def run(self, data):
        return None                      # the base class does not know HOW to compute – each child writes its own run()

    def report(self, data):
        result = self.run(data)          # calls run() of the CHILD (polymorphism!)
        return f"{self.name}: {result}"

    def __str__(self):
        return f"Analysis: {self.name}"

class CountBy(Analysis):
    def __init__(self, column):
        # Step 1: the name:  
        super().__init__("count by " + column)

        # Step 2: remember the column 
        self.column = column
        
    # Step 3: the answer:  data.count_by(self.column)
    def run(self, data):
        return data.count_by(self.column)

class GroupMean(Analysis):
    def __init__(self, group, value):
        # Step 4: the name:  
        super().__init__(f"mean {value} by {group}")
        # Step 5: remember both:  
        self.group = group 
        self.value = value
        
    # Step 6: the answer:  data.group_stat(self.group, self.value)
    def run(self, data):
        return data.group_stat(self.group, self.value)

class TopGroups(GroupMean):           # a child of GroupMean, not of Analysis!
    def __init__(self, group, value, n=3):
        # Step 7: let GroupMean save group and value:  
        super().__init__(group, value)
        # Step 8: remember 
        self.n = n
        # Step 9: overwrite the name: 
        self.name = f"top {n} {group} by mean {value}"
        
    def run(self, data):
        # Step 10: the means from GroupMean:  
        means = super().run(data)
        # Step 11: sort them, biggest first, keep n:
        return sorted(means.items(), key=lambda pair: pair[1], reverse=True)[:self.n]
        
class Filter:
    # Step 1: remember the column:  self.column = column
    def __init__(self, column):
        self.column = column

    # Step 2: the base filter keeps EVERY row:  return True   (children change this)
    def keep(self, row):
        return True  

    # Step 3: like where() in your Dataset, but ask self.keep(row) instead of row[column] == value:
    #         kept = [row for row in data.rows if self.keep(row)]
    #         return Dataset(kept, f"{data.name} | {self}")
    def apply(self, data):
        kept = [row for row in data.rows if self.keep(row)]
        return Dataset(kept, f"{data.name} | {self}")

    # Step 4: print(Filter("HP")) → "filter on HP"
    def __str__(self):
        return f"filter on {self.column}"


class Equals(Filter):
    # Step 5: the parent saves column, you save value:  super().__init__(column)  and  self.value = value
    def __init__(self, column, value):
        super().__init__(column)
        self.value = value

    # Step 6: keep the row when  row[self.column] == self.value
    def keep(self, row):
        return row[self.column] == self.value

    # Step 7: "Type 1 = Water"   hint: f"{self.column} = {self.value}"
    def __str__(self):
        return f"{self.column} = {self.value}"


class Above(Filter):
    # Step 8: like Equals, but save limit:  super().__init__(column)  and  self.limit = limit
    def __init__(self, column, limit):
        super().__init__(column)
        self.limit = limit

    # Step 9: keep the row when the value is not None AND bigger than limit:
    #         row[self.column] is not None and row[self.column] > self.limit
    def keep(self, row):
        return row[self.column] is not None and row[self.column] > self.limit

    # Step 10: "Attack > 100"
    def __str__(self):
        return f"{self.column} > {self.limit}"

        
