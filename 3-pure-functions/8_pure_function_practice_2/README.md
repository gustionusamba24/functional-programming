# Pure Functions Practice
Datetimes are infamously a [pain in the neck](https://gist.github.com/timvisee/fcda9bbdff88d45cc9061606b4b923ca) for programming. One of the easier items on the long list of problems is the order of the year, month, and day in a calendar date. Most of the world uses the day-month-year format, but some [insane countries](https://iso.mit.edu/americanisms/date-format-in-the-united-states/) use month-day-year because they want everyone else to be miserable.

## Assignment
**Refactor the `sort_dates` function**. It currently uses `.sort()`, which modifies the list in-place (an impure operation). We want to change it to use [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) with a custom helper function, to sort the dates chronologically without modifying the original list.
1. Define a helper function named `format_date` outside of `sort_dates`.
    1. It should accept a single string (a date) in `"MM-DD-YYYY"` format (e.g. `"10-14-1995"`).
    2. Inside the function, split the input string and rearrange it to return a new string in `YYYYMMDD` format. For example: `10-05-2023` → `20231005`.
2. Update the `sort_dates` function.
    1. It should accept a list of date strings.
    2. It should return a new sorted list using the built-in `sorted()` function.
    3. Pass your `format_date` function as the `key` parameter to `sorted()`.

> 💡 When you pass `key=format_date`, Python runs your helper function on every item to figure out the sort order (using the `YYYYMMDD` format), but it puts the original dates (`MM-DD-YYYY`) into the final list.