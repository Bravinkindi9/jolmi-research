# Results

## The Flood, Mapped

We ran the before-and-after comparison on Sentinel-1 images over the Nyabihu/Ngororero area for the May 2–3, 2023 flood. At our main cutoff (−3 dB), the method found about **69.1 hectares** of newly flooded land — roughly the size of 100 football pitches, sitting in the low-lying areas near the district's rivers.

We checked this visually in QGIS against a satellite map, and the flagged areas line up with real valleys, not scattered across hillsides or ridges. That matters: if the flagged spots had shown up on ridgelines instead, it would likely mean we were picking up radar shadow (a common false alarm in mountainous terrain) rather than actual floodwater. What we found instead looks like real flooding — water sitting and moving along the lowest parts of the land.

## How Much Does the Cutoff Point Matter?

Picking the flood/no-flood cutoff is a judgment call, not a fixed rule, so we tested how much that choice actually changes the answer. Running the same method at −2 dB and −4 dB gave a noticeably different picture:

| Threshold | Flooded Area |
|---|---|
| −2 dB (more lenient) | 150.05 hectares |
| −3 dB (primary result) | 69.12 hectares |
| −4 dB (more conservative) | 45.20 hectares |

A roughly threefold range between the most lenient and most conservative estimate is a real limitation worth stating plainly: this method does not produce one single "correct" number, it produces a defensible range that depends on how strict a definition of "flooded" is applied. We treat 69 hectares as our headline figure, consistent with commonly used thresholds in the literature, while reporting the full 45–150 hectare range as the more honest representation of what the underlying data supports.

## What Didn't Work: Automatic Thresholding

Attempting to replace the manual threshold with Otsu's automatic method — the same technique used successfully in the only prior Sentinel-1 flood study conducted in Rwanda — produced a very different, and clearly unreliable, result: an estimated **13,939 hectares** of "flooding," more than 200 times larger than our manual result and geographically implausible for the area studied.

This wasn't a coding error. Examining the underlying histogram of pixel values showed why: the method requires the data to naturally split into two distinct groups (flooded and non-flooded), and our data didn't — it formed a single, smooth distribution with no clear separation for the algorithm to detect. The result is a genuine, evidence-backed finding rather than a technical failure to hide: **automatic thresholding, validated elsewhere in Rwanda's flatter river floodplains, does not transfer cleanly to the steep, mixed terrain of the country's western districts.**

## Summary of Findings

| Metric | Result |
|---|---|
| Primary flood extent (−3 dB) | 69.12 ha |
| Sensitivity range (−4 to −2 dB) | 45.20 – 150.05 ha |
| Otsu automatic threshold result | 13,939 ha (rejected as unreliable) |
| Visual validation | Confirmed — flood pattern aligns with valley terrain |

Taken together, these results support two claims central to this study: first, that free, open Sentinel-1 data can meaningfully detect real flood extent in Rwanda's western terrain using a straightforward, low-cost method; and second, that the *reliability* of more advanced, automated versions of that method is not guaranteed to hold across Rwanda's varied terrain — a distinction with direct implications for how confidently this kind of free data can be relied upon in operational, real-world disaster response.
