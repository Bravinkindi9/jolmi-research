# Discussion

The results of this brief point to a straightforward but important conclusion:
a Sentinel-1 SAR flood-detection pipeline built entirely from free, open-access
tools performs fast enough to be operationally interesting, but its automatic
thresholding behavior breaks down in ways that matter specifically because of
where Rwanda's terrain sits.

The clearest evidence for this is the Otsu automatic-thresholding failure. When
applied to the Nyabihu/Ngororero AOI, Otsu's method produced a grossly inflated
flood extent rather than a usable threshold. This is not, on its own, proof
that mountainous terrain defeats SAR-based flood detection outright — the
failure is a known limitation of Otsu's method under class-imbalanced or
unimodal backscatter distributions, and it is documented elsewhere in the
remote sensing literature independent of terrain. What this brief can say with
confidence is narrower and more honest: in this AOI, under this pipeline,
automatic thresholding did not work, and a manual threshold (−3 dB, VV) was
required to produce a usable flood mask instead. Whether that failure was
driven primarily by terrain-induced backscatter heterogeneity (layover, shadow,
mixed hillslope signal) or simply by the class-imbalance conditions of this
particular scene is a question this brief's method cannot fully separate out.
That distinction matters and is worth stating plainly rather than implying a
terrain-specific discovery the data doesn't fully support.

Where this brief's findings differ concretely from Forsberg and Ferdfelt
(KTH, 2024) is that their Lower Nyabarongo study reports no equivalent
thresholding failure — their abstract describes successful automatic Otsu
thresholding with high agreement against UNOSAT reference data. The Lower
Nyabarongo catchment is a flatter, wider floodplain; the Nyabihu/Ngororero
AOI is steep, hilly terrain typical of Rwanda's Western Province. The
contrast between a successful automatic threshold in one AOI and a failed
one in the other is suggestive of a terrain effect, even though this brief
cannot isolate terrain as the sole causal variable with the data collected
here.

On processing latency: once a Sentinel-1 scene was available in Google Earth
Engine's public catalog, this pipeline returned a flood extent result to the
user in a median of 3.36 seconds (range 2.99–3.58s, n=3 runs). This is fast
enough that, in principle, the compute step itself would not be the
bottleneck in a disaster-response timeline. The practical bottleneck for
operational use is more likely to sit elsewhere: satellite revisit frequency,
cloud-free/SAR scene availability timing, manual threshold-tuning effort
(since automatic thresholding failed here and required a human to set the
value), and the time needed to export, validate, and distribute the result
to responders. A fast processing step does not by itself make a pipeline
operationally viable if a human still has to manually inspect and correct
the threshold each time — which is what happened in this case study.

Taken together, the two findings connect: the same terrain that likely
contributes to the Otsu failure is also what would keep this pipeline from
being a fully automated, unattended operational tool. Speed is not the
limiting factor here; automation reliability in complex terrain is.

# Limitations

This brief is a solo, secondary/open-data research exercise with no
fieldwork, no ground-truth validation, and no independent accuracy
assessment against a reference dataset such as UNOSAT's. This is a material
difference from Forsberg and Ferdfelt, who validated their results against
field observations and UNOSAT reference data; this brief's flood extent
estimates should be read as unvalidated pipeline output, not
accuracy-assessed results.

The AOI used here is a rough bounding box over the Nyabihu/Ngororero area,
not an official district shapefile boundary. Reported hectare figures are
therefore approximate to the box drawn, not to the administrative or
hydrological boundary of the affected districts.

The Otsu thresholding failure is interpreted here as suggestive of a
terrain effect but is not proven to be one. Distinguishing a genuine
terrain-driven backscatter effect (layover, shadow, mixed-slope signal)
from an ordinary class-imbalance failure of Otsu's method — which is a
documented general limitation of the algorithm, independent of terrain —
would require a dedicated geometric terrain-correction analysis (e.g.
incidence-angle correction, DEM-based layover/shadow masking) that falls
outside the scope of this brief.

The processing latency figure (median 3.36s) is a single-session,
single-network observation made from one machine and one internet
connection at one point in time. It is not a controlled benchmark, was not
repeated across multiple networks, days, or GEE server-load conditions, and
should not be read as a general claim about GEE's typical response time.
It also excludes asynchronous raster export to Drive, which was not timed
and can take substantially longer depending on GEE's task queue.

The manual threshold (−3 dB, VV) used for the reported flood extent was
selected through visual inspection and sensitivity testing across a range
of values, not through a statistically automated or independently
validated method. This introduces a degree of subjectivity that automatic
thresholding, had it worked, would have removed.

Finally, this brief relies on a single flood event (May 2–3, 2023) and a
single AOI. No claim is made here about generalizability to other flood
events, other mountainous regions of Rwanda, or other countries.

# Conclusion

This brief set out to test how a low-cost, open-data Sentinel-1 SAR flood
detection pipeline performs in the mountainous terrain of Rwanda's Western
Province, and what its observed processing latency implies for its
viability as a disaster-response tool. Using the May 2–3, 2023
Nyabihu/Ngororero floods and landslides as a case study, two findings stand
out.

First, automatic thresholding via Otsu's method — the same method used
successfully in the comparable Lower Nyabarongo study — failed here,
requiring a manual threshold instead. This brief cannot fully separate
terrain-driven causes from the algorithm's known general limitations, but
the contrast with a flatter-terrain study that did not encounter this
failure is a meaningful signal worth further investigation.

Second, once a Sentinel-1 scene is available, the pipeline's own processing
step is fast — a few seconds, not hours. The genuine bottleneck to
operational use is not compute speed but the reliability of automated
thresholding in complex terrain, which currently still requires manual
human judgment to correct.

Together, these findings suggest that a free, GEE-based Sentinel-1 pipeline
is a technically feasible starting point for flood monitoring in Rwanda's
Western Province, but not yet a fully automated, unattended tool for
operational disaster response in mountainous terrain. The most useful next
step for future work — whether by this author or others — would be a
dedicated terrain-correction analysis (incidence-angle and DEM-based
layover/shadow masking) to determine how much of the Otsu failure is
genuinely terrain-driven, paired with a properly controlled, multi-session
latency benchmark to replace the single-session estimate reported here.
