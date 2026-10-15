#!/usr/bin/env python3
# Aerator Math oracle - mirrors engine.js float-for-float.
import json, math
OVERLAP = 0.85
WALKFT = 132
FIRST = 0.65
SECOND = 0.85
PLUGBAR = 2.5
PATTERN = 0.6
HOLEBAR = 4
def r1(x): return math.floor(x*10+0.5)/10
def f1(x): return "%.1f" % r1(x)
def jsnum(x):
    i = int(x)
    return i if x == i else x

def coverage_plan(claim, sqft):
    if not (claim > 0): return {"error": "the claimed inches must be above zero"}
    if not (sqft > 0): return {"error": "the square feet must be above zero"}
    honest_raw = claim * OVERLAP
    rate_raw = honest_raw / 12 * WALKFT
    min_raw = sqft / rate_raw
    verdict = "done before the game" if min_raw <= 30 else ("a working morning" if min_raw <= 75 else "a two-coffee yard")
    return {"honestIn": jsnum(r1(honest_raw)), "minutes": jsnum(r1(min_raw)), "verdict": verdict}
def render_coverage(r, claim, sqft):
    min_word = "1 minute" if r["minutes"] == 1 else f1(r["minutes"]) + " minutes"
    return ("The %s-inch drum honestly covers %s inches after the 0.85 overlap norm; %s square feet at the 1.5-mile-an-hour walk norm takes %s - %s."
            % (claim, f1(r["honestIn"]), sqft, min_word, r["verdict"]))

def depth_plan(claim):
    if not (claim > 0): return {"error": "the claimed inches must be above zero"}
    first_raw = claim * FIRST
    second_raw = claim * SECOND
    verdict = "one run to real plugs" if first_raw >= PLUGBAR else ("two runs to real plugs" if second_raw >= PLUGBAR else "aeration by name only")
    return {"firstIn": jsnum(r1(first_raw)), "secondIn": jsnum(r1(second_raw)), "verdict": verdict}
def render_depth(r, claim):
    return ("The %s-inch claim honestly pulls %s-inch plugs on the first run and %s on the second (labeled norms); against the 2.5-inch plug bar, %s."
            % (claim, f1(r["firstIn"]), f1(r["secondIn"]), r["verdict"]))

def pattern_plan(claim_holes):
    if not (claim_holes > 0): return {"error": "the claimed holes must be above zero"}
    honest_raw = claim_holes * PATTERN
    verdict = "a real pattern" if honest_raw >= HOLEBAR else ("a sparse pattern, honestly" if honest_raw >= 2 else "aeration theater")
    return {"honestHoles": jsnum(r1(honest_raw)), "verdict": verdict}
def render_pattern(r, claim_holes):
    return ("The %s-holes-a-square-foot claim honestly lands %s after the 0.6 pattern norm; against the 4-hole bar, %s."
            % (claim_holes, f1(r["honestHoles"]), r["verdict"]))

CASES = [
    ("coverage", (19,5000)), ("coverage", (16,3000)), ("coverage", (21,8000)),
    ("coverage", (18,12000)), ("coverage", (14,15000)), ("coverage", (26,2000)),
    ("depth", (4,)), ("depth", (3,)), ("depth", (2,)),
    ("depth", (4.5,)), ("depth", (2.5,)), ("depth", (5,)),
    ("pattern", (6,)), ("pattern", (8,)), ("pattern", (2,)),
    ("pattern", (10,)), ("pattern", (3,)), ("pattern", (7,)),
    ("coverage", (0,5000)), ("coverage", (19,0)),
    ("depth", (0,)),
    ("pattern", (0,)),
]
PLANS = {"coverage": (coverage_plan, render_coverage), "depth": (depth_plan, render_depth), "pattern": (pattern_plan, render_pattern)}
out = []
for tool, args in CASES:
    plan, render = PLANS[tool]
    r = plan(*args)
    case = {"tool": tool, "args": list(args), "result": r}
    if "error" not in r:
        case["render"] = render(r, *args)
    out.append(case)
print(json.dumps(out, separators=(",", ":")), end="")
