# Week 1 mini-project: Mad-libs and unit converter

Two small command-line programs from Week 1 of Zero to Hired.

## unit_converter.py

Converts kilometres to miles, kilograms to pounds, and a number of minutes into hours and minutes.

**Sample run**
```
Kilometres: 10
Kilograms: 10
Minutes: 100
10.0 km = 6.21371 miles
10.0 kg = 22.0462 lbs
100 min = 1 h 40 min
```

## mad_libs.py

Asks for a name, an adjective, a noun, a verb, a place and a number, then prints a four-line silly news story using them.

**Sample run**
```
Name: sara
Adjective: old
Noun: banana
Verb: dance
Place: Karachi
Number: 3
While walking home, Sara noticed something bizarre happening down the street.
A group of street performers were danceing right in front of a old banana.
A crowd quickly gathered, causing a massive traffic jam that backed up all the way to Karachi.
The police arrived to clear the road, but it took them 4 hours just to move the crowd. - Reported by Agent S.
```

## How to run
```
python unit_converter.py
python mad_libs.py
```

## Concepts used
`input()` and type conversion (`float`, `int`) · arithmetic with `//` and `%` ·
f-strings · slicing (`name[:1]`) · string methods (`.title()`, `.lower()`)

## Known limitations

**unit_converter.py**
- Crashes with a `ValueError` if any prompt gets non-numeric input, e.g. `ten` or an empty line
- Decimal minutes are silently cut: `90.5` becomes `90`, because `int(float(...))` drops the decimal without warning
- Negative minutes give a misleading result: `-30` prints `-1 h 30 min`, because `//` rounds down rather than towards zero

**mad_libs.py**
- Verbs get `"ing"` added blindly, so `run` becomes `runing` and `make` becomes `makeing`
- A blank or text Number raises a `ValueError` on line 6; decimals like `3.9` are silently cut to `3`
- Blank words don't crash, they just look odd (a blank name gives `Agent .`), because slices never fail and nothing checks the input
- Grammar slips: `a {adjective}` gives `a old` instead of `an old`, and Number `0` gives `1 hours`
