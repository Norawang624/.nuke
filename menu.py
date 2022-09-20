#	------------------------
#	menu.py
#	Version: 1.0.0
#	Last Updated: Sep-20-2022
#	------------------------



import sys
import nuke

import pixelfudger
nuke.knobDefault('Write.channels','rgba')
import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui()

import platform

# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\yoo32\.nuke'
Mac_Dir = ''
Linux_Dir = '/home/cnwang/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = Mac_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None

toolbar = nuke.menu('Nodes')
NW = toolbar.addMenu('CNW', icon='V_Victor.png')

NW.addCommand("Filter/VectorExtendEdge", 'nuke.createNode("VectorExtendEdge")')
NW.addCommand("Filter/EdgeExtend", 'nuke.createNode("EdgeExtend")')
NW.addCommand("Filter/EdgeExtend2", 'nuke.createNode("EdgeExtend2")')
NW.addCommand("Filter/KillOutline", 'nuke.createNode("KillOutline")')
NW.addCommand("Filter/Mix_Fine_Detail_F", 'nuke.createNode("Mix_Fine_Detail_F")')
NW.addCommand("Filter/Edge_RimLight", 'nuke.createNode("Edge_RimLight")')
NW.addCommand("Filter/Fractal_Blur", 'nuke.createNode("Fractal_Blur")')


NW.addCommand("Defocus/OpticalZDefocus", 'nuke.createNode("OpticalZDefocus")')

NW.addCommand("Matte/V_EdgeMatte", 'nuke.createNode("V_EdgeMatte")')

NW.addCommand("Grain/DasGrain", 'nuke.createNode("DasGrain")')
NW.addCommand("Grain/DegrainHelper", 'nuke.createNode("DegrainHelper")')
NW.addCommand("Grain/RemoveGrain", 'nuke.createNode("RemoveGrain")')

NW.addCommand("Animation/AnimationCurve", 'nuke.createNode("AnimationCurve")')
NW.addCommand("Animation/ITransform", 'nuke.createNode("ITransform")')


NW.addCommand("CC/apChroma1", 'nuke.createNode("apChroma1")')
NW.addCommand("CC/ColorSampler", 'nuke.createNode("ColorSampler")')

NW.addCommand("FX/P_Blood_Hit_v5", 'nuke.createNode("P_Blood_Hit_v5")')

NW.addCommand("Key/Filler_Sampler", 'nuke.createNode("Filler_Sampler")')

