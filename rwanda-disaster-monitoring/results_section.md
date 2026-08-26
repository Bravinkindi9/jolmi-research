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

That's roughly a threefold swing between the loosest and strictest cutoff, and it's a real limitation we want to be upfront about. There's no single "correct" number here — just a range that depends on how strict you want to be about what counts as flooded. We're using 69 hectares as our headline number because it matches the cutoff most commonly used in similar studies, but the honest answer is really "somewhere between 45 and 150 hectares."

## What Didn't Work: Letting the Computer Pick the Cutoff

We also tried Otsu's method — an algorithm that picks the cutoff automatically instead of a person choosing it. It's the same method a previous Rwanda flood study used successfully. For us, it didn't work: it estimated **13,939 hectares** of flooding, over 200 times bigger than our manual result and obviously way too much for the area we studied.

This wasn't a bug in our code. When we looked at the underlying data, the reason became clear: Otsu's method needs the data to split into two clear groups — flooded and not flooded — and works best when both groups make up a reasonably balanced share of the image. Our flooded area was a small sliver of a much larger scene, so the data didn't split into two groups at all; it formed one single, smooth curve with no real gap to find. This is a known limitation of the method in general, not something specific to Rwanda. What we can say honestly is that a method that worked on a different, larger floodplain study didn't carry over cleanly to our smaller, more mixed-terrain study area without further adjustment.

It's also worth noting plainly: this exact flood event was already mapped by the UN Satellite Centre (UNOSAT) using Sentinel-1 radar alongside high-resolution optical imagery. We see this study's contribution not as mapping the event better than that response, but as testing how far a simple, free, single-satellite method can get on its own — a relevant question for institutions without access to that kind of multi-sensor support.

## Summary of Findings

| Metric | Result |
|---|---|
| Primary flood extent (−3 dB) | 69.12 ha |
| Sensitivity range (−4 to −2 dB) | 45.20 – 150.05 ha |
| Otsu automatic threshold result | 13,939 ha (rejected — known statistical limitation, not a terrain-specific effect) |
| Visual validation | Confirmed — flood pattern aligns with valley terrain |

Put together, these results back up two main points: free Sentinel-1 data can genuinely detect real flooding in Rwanda's western terrain using a simple, low-cost method — and the more advanced, automatic version of that method can't be trusted to work the same way everywhere in the country. That second point matters a lot if anyone is thinking about relying on this kind of data for real disaster response.
