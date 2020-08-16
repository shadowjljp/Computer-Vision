# Computer-Vision
Computer Vision - Color spaces manipulation

Color changes: xyz_histeq(OpenCV) and xyz_classhisteq (self implementation algorithm) are the only programs that will cause color changes. 
Other programs either have no visible changes or brightness changes.

The lab_lscl,luv_lscl,xyz_lscl programs with linear stretching have very little difference

while the xyz might be the worst because it may cause a dark brown spot on the image after transition among color spaces.
One more thing worth noticing is that luv_histeq has a better overall performance in terms of brightness, color, contrast than xyz_histeq.
The latter one will cause some color shift and in my example the image becomes more lean to red.
