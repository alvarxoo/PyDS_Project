"""cleaning.py – Lab 5: find and handle bad data.

WHAT GOES HERE
    Rules that decide whether a row is valid, exceptions for invalid data,
    a generator that yields only the good rows and a report of what was
    removed and why. Never change the raw file – clean in code.

EXAMPLE (reference project – basketball shots)
    validate(row)                      raises DataError("missing coordinates")
    clean = list(valid_rows(rows, report))
    report -> {"missing value": 0, "half-court heave": 517}
"""

# Your code from Lab 5 goes below.
import time


REQUIRED = ["famsize", "Medu", "Fedu", "studytime", "schoolsup", "Walc", "absences", "G3"]
NON_NEGATIVE = ["Medu", "Fedu", "studytime", "Walc", "absences", "G3"]


def check_row(row, required, non_negative):
    # for every column in required:
    #     if row[column] is None → raise ValueError(f"{column} is missing")
    for column in required:
      if row[column] is None:
        raise ValueError(f"{column} is missing")
    # for every column in non_negative:
    #     if the value is not None AND it is below 0 → raise ValueError(f"{column} is negative")
    for column in non_negative:
      if row[column] is not None and row[column] < 0:
        raise ValueError(f"{column} is negative")

def valid_rows(rows, report, required, non_negative):
    for row in rows:
        # try: call check_row(row, required, non_negative)
        # except ValueError as e:  message = str(e),  count it like in 2.3 b,  then  continue  (skip to the next row)
        try:
          check_row(row, required, non_negative)
        except ValueError as e:
          message = str(e)
          report[message] = report.get(message, 0) + 1
          continue
        # the row is good → give it out with yield
        yield row

    
def timed(func):
  def wrapper(*args, **kwargs):
        # remember the start time: start = time.perf_counter()
        start = time.perf_counter()
        # call the original function with *args, **kwargs and keep its result
        result = func(*args, **kwargs)
        # print how long it took:  print(f"{func.__name__} took {time.perf_counter() - start:.4f} s")
        # print the function name and the time:  f"{func.__name__} took {time.perf_counter() - start:.4f} s"
        print(f"{func.__name__} took {time.perf_counter() - start:.4f} s")
        # give back the result
        return result
  return wrapper


# put the decorator above the def:  @timed
@timed
def clean(rows, required, non_negative):
    # make an empty dictionary report
    report = {}
    # kept = a LIST of everything valid_rows(...) gives   hint: list(valid_rows(rows, report, required, non_negative))
    kept = list(valid_rows(rows, report, required, non_negative))
    # give back both:  return kept, report
    return kept,report

