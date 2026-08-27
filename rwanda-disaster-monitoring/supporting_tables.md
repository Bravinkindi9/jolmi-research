# Supporting Tables

## Table 1: Threshold Sensitivity (VH/VV, dB threshold vs. flooded extent)

**STATUS: placeholder — needs your real sweep data before use.**
Fill in the "Flooded Area (ha)" column by re-running the GEE script at each
threshold value below, at −3 dB VV as the reporting config, with a few
values on either side for the sensitivity curve. Do not publish this table
until every cell has a real, run-produced number.

| Threshold (dB) | Polarization | Flooded Area (ha) | Notes |
|---|---|---|---|
| -2 | VV | *(run and fill in)* | |
| -3 | VV | *(run and fill in — this is your reporting value)* | Final reported threshold |
| -4 | VV | *(run and fill in)* | |
| -5 | VV | *(run and fill in)* | |
| -6 | VV | *(run and fill in)* | |

## Table 2: Sentinel-1 Scene Summary (confirmed from GEE console output)

| Parameter | Value |
|---|---|
| Before-period window | 2023-04-15 to 2023-04-30 |
| After-period window | 2023-05-03 to 2023-05-10 |
| Before images found | 4 |
| After images found | 4 |
| Post-flood scene acquisition time (first after-image) | 2023-05-03 16:20:55 UTC |
| Compositing method | Mean mosaic, before and after |
| Speckle filtering | 50 m circular focal mean |

## Table 3: Observed Processing Latency (own pipeline, timed runs)

| Run | Observed End-to-End Latency (s) | Config |
|---|---|---|
| 1 | 3.576 | -4 dB, VH (timing-test config) |
| 2 | 3.356 | -4 dB, VH (timing-test config) |
| 3 | 2.991 | -4 dB, VH (timing-test config) |
| **Median** | **3.356** | |
| **Range** | **2.991 – 3.576** | |

**Note:** this timing test was run at −4 dB / VH, not the −3 dB / VV
reporting configuration, since it was originally built to validate the
timer mechanism. If you want the latency figure reported alongside your
final −3 dB / VV results, this should ideally be re-run at −3 dB / VV
for consistency — a reviewer could otherwise ask why the timed run and
the reported flood-extent run used different settings. Recommend re-timing
3 runs at −3 dB / VV before this goes into the brief.
