// ============================================
// Sentinel-1 SAR Flood Detection
// Event: May 2-3, 2023 floods/landslides
// Site: Nyabihu / Ngororero, Western Province, Rwanda
//
// PURPOSE:
// Detects flooded areas by comparing radar backscatter ("before" vs
// "after" the flood event). Water reflects radar away from the sensor
// (specular reflection), so flooded pixels show a sharp DROP in
// backscatter (dB) between the before and after images.
//
// OUTPUTS:
// 1. beforeFiltered / afterFiltered - grayscale radar images (context)
// 2. flooded - binary mask (1 = flooded, nodata = not flooded)
// 3. floodedAreaHa - estimated flooded area in hectares
//
// SENSITIVITY CHECK (run 2026-08): threshold tested at -2, -3, -4 dB
//   -4 dB -> 45.20 ha
//   -3 dB -> 69.12 ha  (used as headline number)
//   -2 dB -> 150.05 ha
// Range reported in methodology as a limitation/robustness check.
// ============================================

// 1. Define Area of Interest (AOI)
// Rough bounding box over Nyabihu/Ngororero - refine with actual
// district shapefile later if higher precision is needed.
var aoi = ee.Geometry.Rectangle([29.20, -1.75, 29.55, -1.50]);

Map.centerObject(aoi, 10);
Map.addLayer(aoi, {color: 'red'}, 'AOI');

// 2. Load Sentinel-1 GRD collection: VH polarization, IW mode
var s1 = ee.ImageCollection('COPERNICUS/S1_GRD')
  .filterBounds(aoi)
  .filter(ee.Filter.eq('instrumentMode', 'IW'))
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))
  .select('VH');

// 3. Define BEFORE and AFTER windows around the event
var beforeStart = '2023-04-15';
var beforeEnd   = '2023-04-30';
var afterStart  = '2023-05-03';
var afterEnd    = '2023-05-10';

var beforeCollection = s1.filterDate(beforeStart, beforeEnd);
var afterCollection  = s1.filterDate(afterStart, afterEnd);

print('Before images found:', beforeCollection.size());
print('After images found:', afterCollection.size());

// 4. Create mosaics (mean) for before/after, then smooth speckle noise
var before = beforeCollection.mean().clip(aoi);
var after  = afterCollection.mean().clip(aoi);

var smoothingRadius = 50; // meters
var beforeFiltered = before.focal_mean(smoothingRadius, 'circle', 'meters');
var afterFiltered  = after.focal_mean(smoothingRadius, 'circle', 'meters');

// 5. Change detection - simple difference (after - before)
var diff = afterFiltered.subtract(beforeFiltered);

// 6. Threshold to flag flooded pixels (water = sharp drop in backscatter)
// NOTE: this threshold is a judgment call, not a fixed law of physics.
// -3 dB used as headline value; see sensitivity check above.
var floodThreshold = -3; // dB drop
var flooded = diff.lt(floodThreshold).selfMask();

// 7. Visualize - toggle layers individually in GEE's Layers panel
Map.addLayer(beforeFiltered, {min: -25, max: 0}, 'Before (VH dB)');
Map.addLayer(afterFiltered, {min: -25, max: 0}, 'After (VH dB)');
Map.addLayer(flooded, {palette: ['blue']}, 'Detected Flood Extent');

// 8. Calculate flooded area in hectares
var floodedAreaHa = flooded.multiply(ee.Image.pixelArea()).divide(10000)
  .reduceRegion({
    reducer: ee.Reducer.sum(),
    geometry: aoi,
    scale: 10,
    maxPixels: 1e9
  });
print('Estimated flooded area (hectares):', floodedAreaHa);

// 9. Export layers for use in QGIS / report figures
Export.image.toDrive({
  image: flooded,
  description: 'Nyabihu_Flood_Mask_May2023',
  region: aoi,
  scale: 10,
  maxPixels: 1e9
});

Export.image.toDrive({
  image: beforeFiltered,
  description: 'Nyabihu_Before_VH_Apr2023',
  region: aoi,
  scale: 10,
  maxPixels: 1e9
});

Export.image.toDrive({
  image: afterFiltered,
  description: 'Nyabihu_After_VH_May2023',
  region: aoi,
  scale: 10,
  maxPixels: 1e9
});
