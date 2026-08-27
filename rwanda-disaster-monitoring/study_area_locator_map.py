"""
Study Area Locator Map — Nyabihu/Ngororero, Rwanda
3-panel atlas-style map: Africa -> Rwanda -> AOI zoom
Requires: geemap, cartoee (comes with geemap), ee (Earth Engine API)

Run this in a Python environment with Earth Engine authenticated
(e.g. Google Colab, or local Jupyter with `earthengine authenticate` done).
"""

import ee
import geemap
from geemap import cartoee
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

ee.Initialize()

# ----------------------------------------------------------------
# 1. Define geometries
# ----------------------------------------------------------------
aoi = ee.Geometry.Rectangle([29.20, -1.75, 29.55, -1.50])

rwanda = ee.FeatureCollection('FAO/GAUL/2015/level0') \
    .filter(ee.Filter.eq('ADM0_NAME', 'Rwanda'))

# District-level boundaries for context (Nyabihu, Ngororero)
districts = ee.FeatureCollection('FAO/GAUL/2015/level2') \
    .filter(ee.Filter.eq('ADM0_NAME', 'Rwanda'))

target_districts = districts.filter(
    ee.Filter.inList('ADM2_NAME', ['Nyabihu', 'Ngororero'])
)

# ----------------------------------------------------------------
# 2. Build the figure with 3 panels
# ----------------------------------------------------------------
fig = plt.figure(figsize=(16, 6))

# --- Panel 1: Africa with Rwanda highlighted ---
ax1 = plt.subplot(1, 3, 1, projection=cartoee.crs.PlateCarree())
africa_region = [-20, -35, 55, 38]  # rough Africa bounding box [W, S, E, N]

# Use a neutral basemap image (blended composite) as backdrop context
blank = ee.Image().paint(
    ee.FeatureCollection('FAO/GAUL/2015/level0'), 0, 1
)
cartoee.add_layer(ax1, blank, region=africa_region, vis_params={'palette': ['grey']})
cartoee.add_layer(ax1, ee.Image().paint(rwanda, 1, 3), region=africa_region,
                   vis_params={'palette': ['red']})
ax1.set_title("Africa — Rwanda highlighted", fontsize=11)
cartoee.add_gridlines(ax1, interval=[20, 20], linestyle=":")

# --- Panel 2: Rwanda with Western Province / AOI box highlighted ---
ax2 = plt.subplot(1, 3, 2, projection=cartoee.crs.PlateCarree())
rwanda_region = [28.8, -2.9, 30.9, -1.0]  # Rwanda bounding box

cartoee.add_layer(ax2, ee.Image().paint(rwanda, 0, 1), region=rwanda_region,
                   vis_params={'palette': ['grey']})
cartoee.add_layer(ax2, ee.Image().paint(districts, 0, 1), region=rwanda_region,
                   vis_params={'palette': ['black']})
cartoee.add_layer(ax2, ee.Image().paint(target_districts, 1, 2), region=rwanda_region,
                   vis_params={'palette': ['orange']})
# Draw the AOI box explicitly
cartoee.add_layer(ax2, ee.Image().paint(ee.FeatureCollection([ee.Feature(aoi)]), 1, 3),
                   region=rwanda_region, vis_params={'palette': ['red']})
ax2.set_title("Rwanda — Nyabihu/Ngororero + AOI", fontsize=11)
cartoee.add_gridlines(ax2, interval=[0.5, 0.5], linestyle=":")

# --- Panel 3: Zoomed AOI with district boundary ---
ax3 = plt.subplot(1, 3, 3, projection=cartoee.crs.PlateCarree())
aoi_region = [29.15, -1.80, 29.60, -1.45]

cartoee.add_layer(ax3, ee.Image().paint(target_districts, 0, 2), region=aoi_region,
                   vis_params={'palette': ['black']})
cartoee.add_layer(ax3, ee.Image().paint(ee.FeatureCollection([ee.Feature(aoi)]), 1, 3),
                   region=aoi_region, vis_params={'palette': ['red']})
ax3.set_title("AOI detail", fontsize=11)
cartoee.add_north_arrow(ax3, text="N", xy=(0.9, 0.9), text_color="black",
                         arrow_color="black", fontsize=14)
cartoee.add_scale_bar_lite(ax3, length=10, xy=(0.05, 0.05), linewidth=3,
                            fontsize=8, color="black", unit="km")
cartoee.add_gridlines(ax3, interval=[0.1, 0.1], linestyle=":")

# ----------------------------------------------------------------
# 3. Shared legend + caption
# ----------------------------------------------------------------
legend_patches = [
    mpatches.Patch(color='red', label='Rwanda / AOI boundary'),
    mpatches.Patch(color='orange', label='Nyabihu / Ngororero districts'),
    mpatches.Patch(color='black', label='District boundaries'),
]
fig.legend(handles=legend_patches, loc='lower center', ncol=3, fontsize=9,
           bbox_to_anchor=(0.5, -0.02))

fig.suptitle("Study Area: Nyabihu/Ngororero, Western Province, Rwanda",
             fontsize=14, fontweight='bold')
fig.text(0.5, -0.08,
         "Data: FAO GAUL 2015 (admin boundaries). AOI: author-defined bounding box, "
         "not official district shapefile — see Limitations.",
         ha='center', fontsize=8, style='italic')

plt.tight_layout()
plt.savefig('study_area_locator_map.png', dpi=300, bbox_inches='tight')
plt.show()
