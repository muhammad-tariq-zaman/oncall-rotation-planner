"""Who is on call, from a weekly rotation roster.

Usage: python3 main.py roster.csv --date 2026-11-05 [--weeks 4]
CSV columns: person,week_start (ISO date, Monday of their week).
The person whose week contains the date is ON CALL; the next
--weeks weeks of the rotation are listed after.
"""
import argparse, csv, sys
from datetime import date, timedelta

def plan(rows, when, weeks):
    slots = sorted((date.fromisoformat(r["week_start"].strip()), r["person"]) for r in rows)
    on_call = None
    for start, person in slots:
        if start <= when < start + timedelta(days=7):
            on_call = person
    upcoming = []
    if slots:
        first = slots[0][0]
        # next weeks after the queried week, in roster order, wrapping round
        idx = 0
        for i, (start, _) in enumerate(slots):
            if start <= when < start + timedelta(days=7):
                idx = i
        for n in range(weeks):
            start, person = slots[(idx + n) % len(slots)]
            upcoming.append((str(start + timedelta(days=7 * n)) if n else str(start), person))
    return on_call, upcoming

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--date", default=None)
    parser.add_argument("--weeks", type=int, default=4)
    args = parser.parse_args(argv)
    when = date.fromisoformat(args.date) if args.date else date.today()
    with open(args.path, newline="", encoding="utf-8") as f:
        on_call, upcoming = plan(list(csv.DictReader(f)), when, args.weeks)
    print(f"On call {when}: {on_call if on_call else 'nobody on the roster'}")
    for start, person in upcoming:
        print(f"Week of {start}: {person}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
