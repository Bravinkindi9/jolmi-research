# Methodology

## Study Area and Event

This study focuses on the Nyabihu/Ngororero corridor in Rwanda's Western Province, one of the districts hit hardest by the flooding and landslides of May 2–3, 2023. The area was chosen deliberately: it sits in the steep, mountainous terrain that characterizes much of western Rwanda — a sharp contrast to the flatter river floodplain covered by the only prior Sentinel-1 flood study done in Rwanda (the Lower Nyabarongo catchment). That contrast is the point. If free satellite data behaves differently in this kind of terrain, this is where we'd expect to see it.

## Data Source

All imagery came from Sentinel-1, a radar satellite operated by the European Space Agency and made freely available through Google Earth Engine. Unlike ordinary satellite cameras, Sentinel-1 doesn't rely on sunlight or clear skies — it sends out its own radar pulses and measures what bounces back, which means it can see through cloud cover, rain, and even darkness. This matters enormously for Rwanda: the same storms that cause flooding also produce the cloud cover that blinds ordinary optical satellites at exactly the moment they're needed most.

We used the VH polarization band, which is generally more sensitive to changes in surface roughness — the property that lets radar distinguish water from land in the first place. Water reflects radar pulses away from the sensor rather than back toward it, so flooded ground shows up distinctly darker than dry ground in the resulting image.

## The Detection Method: Before-and-After Comparison

The core method is straightforward: compare a "before" image against an "after" image of the same location, and flag anywhere the signal dropped sharply.

- **Before window:** April 15–30, 2023 — the weeks leading up to the event, capturing normal, pre-flood ground conditions.
- **After window:** May 3–10, 2023 — immediately following the flooding.

Both windows were averaged into single composite images and lightly smoothed (a 50-meter focal mean filter) to reduce speckle — the grainy, salt-and-pepper noise that's a natural byproduct of how radar imaging works, not a flaw in the data itself.

We then subtracted the "before" image from the "after" image. Where the value dropped sharply, that's a strong signal that dry land turned into standing water.

## Setting the Threshold: Manual, With a Sensitivity Check

Turning that continuous drop-in-signal map into a yes/no flood map requires picking a cutoff: how big a drop counts as "flooded"? We started with a commonly used starting point in SAR flood literature, a 3 decibel drop, and treated it as a working default rather than an assumed truth.

To test how much that choice actually mattered, we reran the same analysis at a 2 decibel and a 4 decibel cutoff. The results:

| Threshold | Estimated Flooded Area |
|---|---|
| −2 dB | 150.05 ha |
| −3 dB (primary) | 69.12 ha |
| −4 dB | 45.20 ha |

The roughly threefold spread between the most lenient and most conservative threshold is a real and honest limitation, not something to gloss over — it means the final number depends meaningfully on a human-set parameter. We report 69 hectares as our headline figure because it sits at the commonly used mid-point in the literature, but we treat the full 45–150 hectare range as the more defensible statement of what the data actually supports.

## Attempting an Automatic Threshold: Otsu's Method, and Why It Failed

A more rigorous alternative to picking a threshold by hand is Otsu's method — an algorithm that analyzes an image's histogram and automatically finds the split point that best separates it into two distinct groups, without a person guessing. It's a well-established technique, and it's the exact method used successfully in the only prior Sentinel-1 flood study conducted in Rwanda, over the Lower Nyabarongo floodplain.

We applied it here, twice, on two different sizes of study area. Both times, it failed in the same way: rather than finding a sensible cutoff, it returned a threshold barely below zero, and the resulting "flood" area exploded to an implausible 13,939 hectares — clearly not a real flood extent.

We didn't take that number at face value. Plotting the underlying histogram confirmed why it failed: Otsu's method assumes the data naturally splits into two separate humps — one for flooded pixels, one for dry ones. Our histogram showed a single, smooth hump instead, with no real separation between the two groups for the algorithm to find. Over the flatter, more uniform Lower Nyabarongo floodplain, that separation apparently exists clearly enough for the method to work. Over the steep, mixed terrain of Nyabihu/Ngororero — hillsides, forest, farmland, and settlement mixed together — it does not.

We treat this as a genuine methodological finding rather than a dead end: it's direct, data-backed evidence that Rwanda's mountainous terrain behaves differently from its river floodplains when it comes to automated SAR flood detection, which is precisely the kind of terrain-dependent limitation this study set out to investigate.

## Validation

The manual-threshold flood extent was exported and visually checked in QGIS against a satellite basemap. The flagged areas sit along recognizable low-lying valley terrain near the district's river corridors, rather than scattered across ridgelines or high ground — the pattern we would expect from real flooding rather than a terrain-shadow artifact, which is a known false-positive risk for SAR-based flood detection in hilly terrain.
