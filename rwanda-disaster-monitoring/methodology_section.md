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

We didn't take that number at face value. Plotting the underlying histogram showed why it failed: Otsu's method needs the data to naturally split into two separate humps — one for flooded pixels, one for dry ones — and works best when those two groups make up a reasonably balanced share of the image. Our flooded area was a small fraction of a much larger scene, so the histogram showed one single, smooth hump instead of two, with no clear separation for the algorithm to find.

This is a known, well-documented limitation of Otsu's method in the wider remote sensing literature — it isn't reliable when the class you're looking for (flooded pixels, in our case) makes up only a small slice of the total image, regardless of terrain. We want to be precise about that rather than overstate our own finding: this isn't evidence that Rwanda's terrain specifically defeats the algorithm — it's an example of a widely known statistical limitation showing up in our data. What it does still tell us, honestly, is that a method validated on a different, larger-scale floodplain study didn't transfer cleanly to this study's tighter, mixed-terrain area without further adjustment (such as tiling the image into smaller sub-regions before thresholding, a standard fix for this exact problem that was outside this study's scope).

## Validation

The manual-threshold flood extent was exported and visually checked in QGIS against a satellite basemap. The flagged areas sit along recognizable low-lying valley terrain near the district's river corridors, rather than scattered across ridgelines or high ground — the pattern we would expect from real flooding rather than a terrain-shadow artifact, which is a known false-positive risk for SAR-based flood detection in hilly terrain. This visual check is a useful sanity test, but it is not a substitute for a formal accuracy assessment against independent ground-truth data, which this study did not attempt.

## What This Method Can't See

It's worth being upfront about what a simple method like this misses, rather than letting the flood-extent number stand alone as if it were the whole picture.

This study's approach only flags pixels where the radar signal got noticeably *weaker* after the flood — the expected pattern for open water. But floodwater doesn't always behave this way. When water surrounds buildings or dense vegetation, the radar signal can bounce off the water and then off a vertical surface (a wall, a tree trunk) straight back to the satellite — a "double-bounce" effect that makes the signal *stronger*, not weaker. A method that only looks for weaker signals, like this one, will systematically miss flooding in villages and riverside forest — arguably the areas where knowing about flooding matters most for a disaster response.

This study also did not apply a terrain-based mask (using elevation and slope data to rule out areas that are physically too high or too steep to flood), which is a standard step in more rigorous SAR flood mapping workflows and would help distinguish real flooding from radar shadow more rigorously than visual inspection alone.

It's also worth noting that this exact event was already mapped by the UN Satellite Centre (UNOSAT), which combined Sentinel-1 radar with high-resolution optical imagery across the Nyabarongo, Sebeya, and Mukungwa river corridors shortly after the disaster. That professional, multi-sensor response is a valuable benchmark, and a natural next step for this work would be comparing this study's free, single-method output against it directly. This study's contribution is not that it maps the event better than that response — it's that it tests how far a simple, freely replicable, single-satellite method can get on its own, which speaks directly to what a resource-constrained institution could realistically do without specialized multi-sensor support.
