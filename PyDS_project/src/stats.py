"""stats.py – Lab 3: functions that compute numbers from your data.

WHAT GOES HERE
    Small, reusable functions (one function = one job) that use loops and
    conditions: averages, percentages, filters, grouping, rankings.
    They take lists / dictionaries from loader.py and return numbers or
    new lists / dictionaries – they do not read files and do not plot.

EXAMPLE (reference project – basketball shots)
    shooting_pct(rows)              -> 0.47
    points_per_shot(rows)           -> 1.09
    group_by(rows, "BASIC_ZONE")    -> {"Restricted Area": [...], ...}
    summary_by(rows, "BASIC_ZONE")  -> ranking of zones by points per shot
"""

# Your code from Lab 3 goes below.
import math


def mean(values, digits=2):
    """The mean of a list of numbers, rounded to `digits` decimals."""
    clean_values = [v for v in values if v is not None]
    if not clean_values:
        return None
    return round(sum(clean_values) / len(clean_values), digits)


def median(values):
    """The middle value of a list of numbers."""
    clean = [v for v in values if v is not None]
    if not clean:
        return None
    ordered = sorted(clean)
    n = len(ordered)
    if n % 2 == 1:
        return ordered[n // 2]
    else:
        return (ordered[n // 2 - 1] + ordered[n // 2]) / 2


def count_by(rows, key):
    """How many rows have each value of the column `key`."""
    counts = {}
    for row in rows:
        v = row[key]
        if v is None:
            continue
        if v not in counts:
            counts[v] = 0
        counts[v] += 1
    return counts


def group_stat(rows, group, value, how="mean"):
    """One number per group: the mean / median / count / max of `value` in every group of `group`."""
    groups = {}
    for row in rows:
        g_val = row[group]
        v_val = row[value]
        if g_val is None or v_val is None:
            continue
        if g_val not in groups:
            groups[g_val] = []
        groups[g_val].append(v_val)

    def one_number(values):
        if how == "median":
            return median(values)
        if how == "count":
            return len(values)
        if how == "max":
            return max(values)
        return mean(values)

    return {k: one_number(v) for k, v in groups.items()}


def std(values, digits=2):
    """The standard deviation (sample): how far the values are from the mean."""
    clean = [v for v in values if v is not None]
    n = len(clean)
    if n <= 1:
        return None
    m = sum(clean) / n
    variance = sum((x - m) ** 2 for x in clean) / (n - 1)
    return round(math.sqrt(variance), digits)


def share(values, digits=2):
    """The share of True values (0-1)."""
    clean = [v for v in values if v is not None]
    if not clean:
        return None
    true_count = sum(1 for v in clean if v is True)
    return round(true_count / len(clean), digits)


def filter_rows(rows, where):
    """The rows for which where(row) is True."""
    return [row for row in rows if where(row)]


def top(result, n=5):
    """The n biggest (key, number) pairs of a dictionary."""
    sorted_items = sorted(result.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_items[:n]


def min_max(values):
    """The smallest and the biggest value as a pair."""
    clean = [v for v in values if v is not None]
    if not clean:
        return None
    return (min(clean), max(clean))


def summary_by(rows, group, value):
    """A table: for every group the number of values and their mean."""
    counts = group_stat(rows, group, value, how="count")
    means = group_stat(rows, group, value, how="mean")
    result = []
    for g in counts:
        result.append({
            "group": g,
            "count": counts[g],
            "mean": means[g]
        })
    return sorted(result, key=lambda item: item["mean"], reverse=True)

