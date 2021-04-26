The design.fsf file contains the details of the first-level FEAT analysis conducted for fmri dataset for a fluency task. 
It has two EVs; Word Generation (WG) and Word Shadowing (WS)
Two contrasts were generated, one for each EV.

Pre-processing comprised of motion correction, and smoothening with a Gaussian kernal of 8 mm FWHM.

Co-registration was performed for the mean fmri image from the functional to the anatomical space using structural_brain.nii.gz as the reference image.
The transformation matrix generated from this was applied to thresh_zstat1.nii.gz and thresh_zstat2.nii.gz to move them to the anatomical space.

The activation areas were viewed in fsleyes using a threshold value of 3.1 (same as that used in FEAT analysis). The screenshots are attached in the report submitted via Google Classroom.
