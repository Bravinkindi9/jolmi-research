# Existing Research and Positioning

## What's Already Been Done

Before treating this study as breaking new ground, it's worth being upfront about what already exists — because two credible efforts have already looked at exactly this event.

**A prior academic study** mapped the same May 2023 floods using Sentinel-1 SAR change detection with automatic (Otsu) thresholding, alongside Sentinel-2 optical imagery and a Random Forest land-cover classifier. Its study area was the Lower Nyabarongo catchment — the broad, lower-relief river floodplain downstream of Kigali. It reported high agreement with a UNOSAT reference dataset, though the exact meaning of that accuracy figure is difficult to independently verify without the full published methodology, and it did not test performance in steeper terrain, did not address commercial data costs, and was not designed to answer an operational or economic question.

**A professional emergency response** also mapped this event directly. The UN Satellite Centre (UNOSAT) activated a formal response, combining Sentinel-1 radar with high-resolution optical imagery to map flood extent across the Nyabarongo, Sebeya, and Mukungwa river corridors — including terrain much closer to this study's own area of interest. This represents an established, multi-sensor, professionally validated workflow, and it is the appropriate benchmark against which any simpler method's outputs should eventually be measured.

## Where That Leaves This Study

Given both of these, the honest research question is not "can Sentinel-1 detect floods in Rwanda" — that has already been answered, more than once, including for this exact event.

The narrower, still-open question this study focuses on instead is: **what can a simple, single-satellite, freely replicable method actually achieve on its own, in Rwanda's steep western terrain specifically, without access to multi-sensor professional tools or specialized processing pipelines?** That's a meaningfully different question from either prior effort. The academic study validated its method over flatter floodplain terrain; the UNOSAT response used professional multi-sensor tooling not readily available to a local institution without significant infrastructure and expertise. Neither addresses what a resource-constrained agency — without a UNOSAT-level response or dedicated remote sensing expertise — could realistically produce on its own using free data and a basic, documented method.

This reframing matters for how the rest of this brief should be read. The technical result here is not presented as an improvement on prior work, or as new evidence that Sentinel-1 works in Rwanda — both of those points are already established. It is presented as evidence toward a different, more practical question: how far does the *simplest possible version* of this approach get you, what does it visibly fail to do, and what would it actually cost or require to close the remaining gap. That question — not flood detection itself — is the actual contribution of this study, and it connects directly to the access and pricing analysis that follows.
