QGIS Plugin for Headland Archaeology
Built for QGIS 3.34
Author: Lei Ding
Date: 2025-03-04
Requirements: QGIS 3.34 or later: This plugin is built for this version of QGIS.



Overview
This QGIS plugin is designed specifically for the GIS Team at Headland Archaeology to assist with project design tasks. It includes functionality to streamline workflows related to the creation of utility buffers and trench stakeout points, based on updated instructions from a Health and Safety company.

Tab 1 - Project Setup
Features
✅ Utility Buffer Creation
This tool helps generate utility buffers based on the latest instructions provided by our Health and Safety partner.

✅ Stakeout Points Creation - Trench
This feature allows you to create trench stakeout points for a selected layer (chosen from the dropdown list in the plugin interface).

Stakeout points are placed at the centroid of the two small ends of the trench.
Note: Stakeout points will only be created for features with the 'Trench' rule if the 'Type' field value is 't'. For other layers, or features that do not meet this condition, use the 'Create Other Stakeout' function instead.
✅ Stakeout Points Creation - Other
This feature allows you to create stakeout points for multiple selected layers (chosen from the layer tree).

Stakeout points are created by extracting vertices.
Note: If the selected layers include a layer with 'Proposed Archaeology' in its name, the plugin will check the 'Type' field and skip features where the value is 't'.
Stakeout points from multiple layers will be merged into a single layer.
✅ Merging Stakeout Points
If both Trench Stakeout Points and Other Stakeout Points checkboxes are selected, the two outputs will be merged into a single stakeout point layer.

✅ Get PRoW by Canvas or Layer
This feature retrieves public path data from the Datto server. It then uses the national grid polygon to determine the site location (based on either the selected canvas area or a specified layer).

The public path is clipped using the grid data and pasted into the master layer, 'Public Path'.
Note: If the 'Public Path' layer has been renamed, the process will abort and raise a warning.


✅ Get Mapping by Canvas or Layer
This feature retrieves OS backmapping data from the Datto server. It then uses the national grid polygon to detect the site location (based on either the selected canvas area or a specified layer).

Each source layer is clipped by the grid data and pasted into the corresponding master layer.



Tab 2 - QC Setup

✅ Check Constraint Conflicts
Selecting this checkbox enables a dropdown menu to choose the 'Proposed Archaeology' layer (must be a polygon layer).
Then, select all the layers to check for conflicts (e.g., Utility layer, HER layer, Ecology layers).
A pop-up window will display any proposed archaeology features that intersect with constraint features, highlighting them in the 'Proposed Archaeology' layer.


✅ Check Machine Travel Space (for Trenches)
Selecting this checkbox enables a dropdown menu to choose the 'Proposed Archaeology' layer (must be a polygon layer).
The plugin checks if there is enough space for machines to travel between features.
The calculation is based on a 2.5m buffer, ensuring a 5m gap between features.
Any feature that does not meet this requirement will be selected, and a pop-up window will indicate the number of features needing further review.
Note: If relocation is not allowed (per client data), please inform the PM.
✅ Check Utility Lines

This function verifies whether any utility line data is located outside a utility buffer zone.
This issue can occur when utility data is frequently updated.
A warning table will pop up, and problematic features in the utility layer will be selected.

✅ Check Layer Directory
This function checks all layers in the layer tree to identify layers stored outside the project home directory.
Web Map Services (WMS) are excluded from this check as they are linked via URLs.
GCAT_raw is also excluded as it is a table.





