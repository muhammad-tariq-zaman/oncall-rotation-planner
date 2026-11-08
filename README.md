# oncall-rotation-planner

Answer 'who is on call?' from a weekly roster CSV, and list the next few weeks of the rotation so cover is never a surprise.

## How to run

```sh
python3 main.py roster.csv --date 2026-11-05 --weeks 4
```

## Example output

```
On call 2026-11-05: Ali
Week of 2026-11-02: Ali
Week of 2026-11-09: Sara
```

Standard library only. Run the tests with `python3 -m unittest discover`.
