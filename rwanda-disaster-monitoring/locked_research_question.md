## Research Question (locked — 27 August 2026)

**How does Sentinel-1 SAR-based flood detection — using a low-cost, open-data
Google Earth Engine pipeline — perform in the mountainous terrain of Rwanda's
Western Province, and what does the pipeline's observed processing latency
imply for its viability as an operational disaster-response tool, using the
May 2–3, 2023 Nyabihu/Ngororero floods and landslides as a case study?**

### Why this framing

A directly overlapping prior study (Forsberg & Ferdfelt, KTH, 2024, DiVA
urn:nbn:se:kth:diva-355853) uses the same core method — Sentinel-1 image
differencing with Otsu thresholding on Google Earth Engine — applied to the
Lower Nyabarongo catchment for the same May 2023 flood period. Verified
against the paper's abstract (cross-checked via two independent research
passes):

- Terrain performance (flat vs. mountainous) is **not discussed** in the
  existing paper.
- Processing/acquisition latency is **not discussed** in the existing paper.
- Nyabihu, Ngororero, and the Western Province landslide disaster are
  **not covered** — the existing paper's AOI is geographically distinct.
- Cost/open-data access **is** already claimed as a contribution by the
  existing paper, so it is retained here as a supporting element rather
  than the primary claim.

This brief's novel contributions are therefore: (1) terrain-specific
pipeline behavior in mountainous topography, evidenced by the Otsu
automatic-thresholding failure documented during methodology testing, and
(2) a first-party measured processing-latency figure.

### Measured latency (first-party, own pipeline)

Median 3.36 seconds (range 2.99–3.58s, n=3 runs), measured as end-to-end
script execution time in the GEE code editor from script start to the
final flood-area result returning to the client, excluding asynchronous
raster export to Drive. Run at −4 dB threshold, VH polarization.

**Limitation to state explicitly in the brief:** this is an observed,
single-session, single-network measurement, not a controlled benchmark.
Latency may vary by network, region, and GEE server load.
