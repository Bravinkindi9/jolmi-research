# The Access Gap: What Free Data Gets You, What Commercial Data Costs, and Where the Real Gap Sits

## What Free Data Actually Gave Us

The flood detection in this study didn't cost a cent beyond time and effort. Sentinel-1 radar data is free, permanently available through Google Earth Engine, and the method used here found roughly 69 hectares of flooding in the Nyabihu/Ngororero area during the May 2023 event — with results ranging from 45 to 150 hectares depending on how the threshold was set.

That's a real result, not a token one. No contracts, no approval process, no minimum spend. Any Rwandan institution — a university, a district office, MINEMA itself — could run this same pipeline today, for free.

But free doesn't mean complete. Two things limit what this data can actually do:

**It doesn't come around often enough.** Sentinel-1 currently revisits any given location roughly every six days. That's fine for slow, rising floods that stay put for days — like the ones in the lower Nyabarongo valley. It's far too slow for the flash floods common in steep catchments like the Sebeya river, where a storm can trigger a flood that rises and drains again within 24 hours. By the time the satellite passes overhead, the water may already be gone.

**It doesn't behave the same everywhere.** This is something we found out firsthand, not something we read in a paper — see the box below.

## Box: Why We Tried — and Dropped — an "Automatic" Method

Most manual flood-mapping methods ask a person to pick a cutoff value by hand: "anything darker than this number, call it flood." That's what we did first, and it worked, but it means a human is making a judgment call.

There's a better-known alternative called **Otsu's method** — an algorithm that looks at an image and finds the best natural dividing line between two groups on its own, without a person guessing. It's commonly used to separate an object from its background in an image. In our case, that would mean the algorithm automatically deciding what counts as "flooded" versus "not flooded," based purely on the data. A previous Rwanda-based study (covering the Lower Nyabarongo river valley) used exactly this method successfully.

We tried it too — and it broke. Not because of a coding mistake, but because Otsu's method only works when an image naturally splits into two distinct groups, like two separate bumps in a chart. When we plotted our own data, we got one single bump, not two — meaning there was no clean "flooded vs. not flooded" split for the algorithm to find. It defaulted to a near-meaningless cutoff, and the flood area it reported ballooned to an obviously wrong 13,000+ hectares.

This isn't a failure to hide — it's a finding. It tells us something real: automatic thresholding works well over the flatter, more uniform floodplain the earlier study covered, but breaks down over the steep, mixed terrain of western Rwanda. That's exactly the kind of terrain difference this study set out to investigate, and now we have direct evidence for it.

## What Commercial Data Costs — Real, Checked Numbers

When free data isn't fast enough or reliable enough — a collapsed bridge, a specific community at risk, a need for imagery within hours — commercial satellite tasking is the alternative. The prices below are pulled straight from Umbra Space's own published pricing page, checked directly, not estimated from a third party.

| What you get | Area covered | Sharpness | Price |
|---|---|---|---|
| Spotlight | 5×5 km (25 km²) | 1.0 m | $675 |
| Spotlight | 5×5 km (25 km²) | 0.25 m | $3,250 |
| Wider shot | 10×10 km (100 km²) | 1.0 m | $1,500 |

For scale: the entire flood area we mapped in this study — 69 hectares — fits comfortably inside a single 25 km² scene. A one-off order to double-check or sharpen this study's free-data result would cost somewhere between $675 and $3,250. That's a reachable amount for a single decision. It adds up fast, though, if you need this kind of imagery regularly rather than once.

## The Options Nobody Talks About

Between "free but limited" and "paid but sharp," there are three paths that get little attention:

**Free during an actual disaster — sort of.** There's an international system called the Charter for Space and Major Disasters. When it's triggered for a real disaster, some commercial providers (ICEYE among them) hand over imagery for free. Rwanda has actually used this — the May 2023 event triggered an activation. But there's a catch: it wasn't Rwanda that pulled the trigger. The request came from a UN agency (UNITAR, on behalf of OCHA) on Rwanda's behalf, not from a Rwandan institution directly. And it only works after a disaster is declared severe enough — it won't help with routine monitoring or catching a flood early.

**A free public archive most people don't know exists.** Since 2023, Umbra has been giving away thousands of real SAR images to the public, free to use, share, and even build on. It won't get you a live image of today's flood, but it's a genuinely useful, currently underused resource for background research, mapping, or training analysis tools — completely free, right now.

**A formal (if slow) route through ESA.** The European Space Agency will pay for commercial satellite access — including ICEYE — on behalf of approved research projects. It means writing a proposal and waiting, but it's a real, existing path for a university project to get commercial-grade data without needing a budget for it.

## So What's the Actual Gap?

The answer isn't "free data is bad" or "commercial data is the fix." It's more specific than that: free Sentinel-1 data is genuinely useful for big, slow floods, but it gets noticeably less reliable in exactly the kind of steep, fast-changing terrain that made the May 2023 disaster so damaging in the first place. Closing that gap doesn't require Rwanda to start buying expensive satellite time across the board — it means either paying for a handful of targeted, high-value scenes when it truly matters, or building better institutional access to the free-but-overlooked routes that already exist — the Charter, Umbra's open archive, ESA's support program — none of which are currently a routine part of how Rwanda responds to floods.
