# Rwanda Disaster Monitoring: Cloud Cover, SAR, and the Cost of Access

**Status:** In progress (paused to focus on CMU-Africa technical test prep)

## Research question
How does cloud cover limit optical satellite-based flood monitoring in
Rwanda during rainy seasons, and can freely available Sentinel-1 SAR data
close that gap — at what cost compared to commercial alternatives?

## Locked case study
May 2-3, 2023 flash floods and landslides, Western Province, Rwanda
(Nyabihu, Ngororero, Rubavu, Rutsiro, Karongi districts).

## Progress so far
- [x] GEE Sentinel-1 SAR change-detection script built and run
      (`scripts/gee/flood_detection_sentinel1.js`)
- [x] Flood extent detected, verified visually in QGIS against
      real terrain (confirmed near valleys, not ridgelines)
- [x] Sensitivity check across -2/-3/-4 dB thresholds:
      45.20 ha / 69.12 ha / 150.05 ha
- [x] Umbra commercial SAR pricing verified live against
      umbra.space/pricing (matches Gemini research report)
- [ ] QGIS figure with basemap, scale bar, legend, north arrow
- [ ] Pricing/access section written up
- [ ] Otsu's thresholding (algorithmic, non-manual threshold) - stretch
- [ ] Pretrained flood-detection model comparison - optional stretch,
      only after core report is complete
- [ ] Full report draft

## Folder structure
```
data/              raw + processed data, event list
scripts/gee/       Google Earth Engine scripts
scripts/analysis/  Python/Colab notebooks for stats + charts
outputs/figures/   exported maps/charts
outputs/tables/    pricing tables, results tables
writing/drafts/    markdown drafts, references.bib
publish/           final assembled report/site files
```

## Key sources
- International Charter Space and Major Disasters (free commercial SAR
  during activated disasters)
- Umbra Open Data Program (CC BY 4.0, free archive SAR)
- ESA Third Party Missions (subsidized ICEYE access for research proposals)

## Tools used
- Google Earth Engine (SAR processing)
- QGIS (visualization, figures)
- Gemini (broad literature/pricing research - verify claims before citing)
