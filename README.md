# Aerator Math

Lawn aerator honesty. The drum is narrower than the decal, the plugs
are shallower than the box, and the yard was always bigger than the
Saturday. Aerator Math turns the claim, the depth and the pattern into
the morning.

Live: https://ilanis-agent.github.io/aeratormath/

## The three truths

1. **The coverage truth** - the claimed drum width x the 0.85 overlap
   norm (labeled) is the honest width; honest inches against the
   1.5-mile-an-hour walk norm (labeled) is the honest clock on the
   lawn: done before the game, a working morning, or a two-coffee
   yard.
2. **The depth truth** - the claimed depth x 0.65 on the first run and
   x 0.85 on the second (labeled norms) against the 2.5-inch plug bar:
   one run to real plugs, two runs to real plugs, or aeration by name
   only.
3. **The pattern truth** - the claimed holes a square foot x the 0.6
   pattern norm (labeled) against the 4-hole bar: a real pattern, a
   sparse pattern, honestly, or aeration theater.

Illustrative arithmetic with labeled norms - not a measurement of your
aerator, your soil or your yard. Follow the manual's safety
instructions.

## Files

- `index.html` - landing page
- `app.html` - the three-truth app
- `engine.js` - pure functions (`coveragePlan`, `depthPlan`, `patternPlan`) plus renderers
- `oracle.py` - independent oracle that mirrors the engine float-for-float
- `test.js` - node tests: engine against oracle output (`node test.js`)
- `expected.json` - oracle-generated cases and renders
