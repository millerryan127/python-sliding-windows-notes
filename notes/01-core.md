# Build fixed-size sliding windows: implementation

## What the example does

Only complete windows are returned. A width larger than the list produces no windows; width must be positive.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "items": [
    1,
    2,
    3,
    4
  ],
  "width": 2
}
```

Expected result:

```json
[
  [
    1,
    2
  ],
  [
    2,
    3
  ],
  [
    3,
    4
  ]
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
