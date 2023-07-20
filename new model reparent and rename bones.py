import bpy

conversion = {
	"lBreast" : "Breast.L",
	"rBreast" : "Breast.R",
	"lNipple" : "Nipple.L",
	"rNipple" : "Nipple.R",
	"lAreola" : "Areola.L",
	"rAreola" : "Areola.R",
}

rigname = 'Genesis 8.1 Female' #Default rig name
for rig in bpy.context.selected_objects:
	if rig.type == 'ARMATURE':
		for b in rig.pose.bones:
			if b.name in conversion:
				tempname = b.name
				for mesh in rig.children:
					if tempname in mesh.vertex_groups:
						mesh.vertex_groups[tempname].name = conversion[tempname]
				rig.pose.bones[tempname].name = conversion[tempname]
		rigname = rig.name #Set the rig name since it was found
		
reparent = {
	"Butt.L" : "pelvis.twk",
	"Butt.R" : "pelvis.twk",
	"Vagina_bone_2" : "genitals",
	"Vagina_bone_1" : "genitals",
	"Vagina_Open" : "Genitals",
	"Rectum_Open" : "Anus",
	"Breath" : "chest.twk",
	"Breath.Belly" : "spine-1.twk"
}

"""
custom_shapes = {
	"Butt.L" : "pelvis.twk",
	"Butt.R" : "pelvis.twk",
	"Vagina_bone_2" : "genitals",
	"Vagina_bone_1" : "genitals",
	"Vagina_Open" : "Genitals",
	"Rectum_Open" : "Anus",
	"Breath" : "chest.twk",
	"Breath.Belly" : "spine-1.twk"
}
"""

arm = bpy.data.objects[rigname]
bpy.ops.object.mode_set(mode='EDIT')
for bone in reparent.keys():
	arm.data.edit_bones[bone].parent = arm.data.edit_bones[reparent[bone]]
	
	#bpy.ops.object.mode_set(mode='POSE')
	#arm.data.pose.bones[bone].custom_shape = bpy.data.objects[]
