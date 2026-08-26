# Limitations

This study is intentionally scoped as a simple, low-cost proof-of-concept, not a comprehensive or operational flood-monitoring system. Several limitations follow directly from that scope, and are worth stating together in one place rather than leaving scattered across sections.

**Single event, single method.** This study examined one flood event, using one detection method, over one area of interest. The results shown here should not be read as a general statement about Sentinel-1's reliability across Rwanda — only as one tested case, in one kind of terrain.

**No detection of flooded buildings or dense vegetation.** Because the method looks only for a drop in radar signal, it cannot detect flooding in areas where a "double-bounce" effect (water reflecting off a vertical surface like a wall or tree trunk) causes the signal to increase instead. This means flooded villages and riverside forest — often the areas of greatest human impact — are not reliably captured by this method as implemented here.

**No terrain-based exclusion mask.** This study relied on visual inspection in QGIS to check that flagged areas aligned with valley terrain, rather than a mathematical mask built from elevation and slope data. Visual inspection is a reasonable sanity check, but it is not a substitute for a rigorous method of ruling out radar shadow, which can otherwise be mistaken for standing water in steep terrain.

**No formal accuracy assessment.** This study did not compare its output against an independent ground-truth dataset (such as the UNOSAT product covering the same event) using standard accuracy metrics. The true precision and recall of this method's output remain unknown, and should be treated as an open question rather than an implied strength.

**Threshold sensitivity.** The final flood extent depends meaningfully on a human-chosen cutoff value, with a roughly threefold range (45–150 hectares) across a small window of reasonable choices. This is reported transparently throughout this study rather than resolved, and represents a genuine source of uncertainty in the headline figure.

**Pricing figures reflect a single point in time.** The commercial pricing cited in this study was verified directly against provider websites at the time of writing, but commercial satellite tasking prices are subject to change, and this study does not account for negotiated enterprise or government contract pricing, which may differ from public list prices.

None of these limitations undermine the core, narrower claim this study makes: that a simple, freely replicable method can produce a real, if imperfect, flood extent estimate in difficult terrain, and that the specific technical gaps it reveals can be tied to concrete, checkable costs. They do mean this study's output should not be treated as authoritative or operationally deployable in its current form.
