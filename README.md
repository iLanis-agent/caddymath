# Caddy Math

Event carnival cupcake caddy, week, cost and time arithmetic. The 290 cupcakes at 12 cupcakes a caddy take 25 caddies, the last caddy holding 2 cupcakes.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The caddies truth** - the cupcakes (1 to 1000000) divided by the cupcakes a caddy (1 to 1000), rounded up, with what the last caddy holds.
- **The weeks truth** - the cupcakes divided by the cupcakes used a week (1 to 100000), with the cupcakes left for the next week.
- **The cost truth** - the caddies (1 to 100000) times the caddy price ($0.01 to $999.99) to the cent, and spread over the cupcakes, half rounded up.
- **The time truth** - the cupcakes divided by the cupcakes packed a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any cupcake, caddy or venue and does not know whether cupcakes will really stay fresh, a supplier will run out or a price will hold, and it gives no verdict that a caddy is worth its price or a cupcake is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every caddy recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
