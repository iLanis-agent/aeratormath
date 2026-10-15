// Aerator Math engine - lawn aerator honesty, labeled norms, honest arithmetic.
(function(root){
"use strict";
var OVERLAP = 0.85; // labeled norm: honest drum width after lane overlap
var WALKFT = 132;   // labeled norm: honest walking pace in feet a minute (about 1.5 mph)
var FIRST = 0.65;   // labeled norm: honest first-run plug depth share of the claim
var SECOND = 0.85;  // labeled norm: honest second-run plug depth share of the claim
var PLUGBAR = 2.5;  // labeled norm: inches a plug needs to count against compaction
var PATTERN = 0.6;  // labeled norm: honest hole pattern share of the claim
var HOLEBAR = 4;    // labeled norm: holes a square foot that make a real pattern
function r1(x){ return Math.round(x*10)/10; }
function f1(x){ return r1(x).toFixed(1); }

function coveragePlan(claimIn, sqft){
  if (!(claimIn > 0)) return { error: "the claimed inches must be above zero" };
  if (!(sqft > 0)) return { error: "the square feet must be above zero" };
  var honestRaw = claimIn * OVERLAP;
  var rateRaw = honestRaw / 12 * WALKFT;
  var minRaw = sqft / rateRaw;
  var verdict = minRaw <= 30 ? "done before the game" : (minRaw <= 75 ? "a working morning" : "a two-coffee yard");
  return { honestIn: r1(honestRaw), minutes: r1(minRaw), verdict: verdict };
}
function renderCoverage(r, claimIn, sqft){
  var minWord = r.minutes === 1 ? "1 minute" : f1(r.minutes) + " minutes";
  return "The " + claimIn + "-inch drum honestly covers " + f1(r.honestIn) + " inches after the 0.85 overlap norm; " + sqft + " square feet at the 1.5-mile-an-hour walk norm takes " + minWord + " - " + r.verdict + ".";
}

function depthPlan(claimIn){
  if (!(claimIn > 0)) return { error: "the claimed inches must be above zero" };
  var firstRaw = claimIn * FIRST;
  var secondRaw = claimIn * SECOND;
  var verdict = firstRaw >= PLUGBAR ? "one run to real plugs"
    : (secondRaw >= PLUGBAR ? "two runs to real plugs" : "aeration by name only");
  return { firstIn: r1(firstRaw), secondIn: r1(secondRaw), verdict: verdict };
}
function renderDepth(r, claimIn){
  return "The " + claimIn + "-inch claim honestly pulls " + f1(r.firstIn) + "-inch plugs on the first run and " + f1(r.secondIn) + " on the second (labeled norms); against the 2.5-inch plug bar, " + r.verdict + ".";
}

function patternPlan(claimHoles){
  if (!(claimHoles > 0)) return { error: "the claimed holes must be above zero" };
  var honestRaw = claimHoles * PATTERN;
  var verdict = honestRaw >= HOLEBAR ? "a real pattern"
    : (honestRaw >= 2 ? "a sparse pattern, honestly" : "aeration theater");
  return { honestHoles: r1(honestRaw), verdict: verdict };
}
function renderPattern(r, claimHoles){
  return "The " + claimHoles + "-holes-a-square-foot claim honestly lands " + f1(r.honestHoles) + " after the 0.6 pattern norm; against the 4-hole bar, " + r.verdict + ".";
}

root.AeratorMath = { coveragePlan: coveragePlan, renderCoverage: renderCoverage, depthPlan: depthPlan, renderDepth: renderDepth, patternPlan: patternPlan, renderPattern: renderPattern };
})(typeof window !== "undefined" ? window : globalThis);
