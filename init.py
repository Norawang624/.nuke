#	------------------------
#	init.py
#	Version: 1.0.0
#	Last Updated: Sep-20-2022
#	------------------------
#	------Define-Custom-Folder-Structure-----


import nuke

nuke.pluginAddPath('pixelfudger')
nuke.pluginAddPath('Gizmo')
nuke.pluginAddPath('icon')
nuke.pluginAddPath('python')
nuke.pluginAddPath('./higx/PointRender')
nuke.pluginAddPath('./NukeSurvivalToolkit')

import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte()

nuke.pluginAddPath('./higx/PointRender')
