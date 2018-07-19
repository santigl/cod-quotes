# CoD Quotes

This files can be used to display a randomly-selected quote from those that
appear when you are killed in the Call of Duty series.

## quote.py
This Python script reads from the `quotes.txt` file, which contains a quote
per line.

```
usage: quote.py [-h] [-u] [-f FILE]

Prints a random quote from Call of Duty

optional arguments:
	-h, --help            show this help message and exit
	-u, --utf8            print pretty punctuation
	-f FILE, --file FILE  read from selected file (default: ./quotes.txt)
```

## Fortune
The `quotes` and `quotes.dat` can be used with the program `fortune`.

`quotes` contains the quotes separated by lines containing `%`, from which the
`.dat` is generated using `strfile`. The `.dat` contains pointers to strings
in `quotes` that allow a quick random access.

## Content
The quotes were taken from this [Wikia article](http://callofduty.wikia.com/wiki/Quoted_sayings_in_the_Call_of_Duty_series).
