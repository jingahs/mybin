import bpy

#Fingers might not work too well if they don't fit the hand. Just move the bone out a bit in edit mode in that case
#Parent the _T and _W bones
#Thighs and pelvis for legs have to be redone
#Parent Head_00 to head

conversion = {
	"hips" :  "pelvis.twk",
	"right_leg_01" :  "thigh.bend.twk.R",
	"right_leg_02" :  "shin.R",
	"right_foot" :  "foot.twk.R",
	"right_toe" :  "toe.R",
	"spine_01" :  "spine.twk",
	"spine_02" :  "spine-1.twk",
	"spine_03" :  "chest.twk",
	"neck" :  "char_neck",
	"head" :  "char_head",
	"right_shoulder" :  "clavicle.R",
	"right_arm_01" :  "upper_arm.bend.twk.R",
	"right_arm_02" :  "forearm.bend.twk.R",
	"right_hand" :  "hand.twk.R",
	"right_thumb_01" :  "thumb.01.R",
	"right_thumb_02" :  "thumb.02.R",
	"right_thumb_03" :  "thumb.03.R",
	"right_index_01" :  "f_index.01.R",
	"right_index_02" :  "f_index.02.R",
	"right_index_03" :  "f_index.03.R",
	"right_middle_01" :  "f_middle.01.R",
	"right_middle_02" :  "f_middle.02.R",
	"right_middle_03" :  "f_middle.03.R",
	"right_ring_01" :  "f_ring.01.R",
	"right_ring_02" :  "f_ring.02.R",
	"right_ring_03" :  "f_ring.03.R",
	"right_pinky_01" :  "f_pinky.01.R",
	"right_pinky_02" :  "f_pinky.02.R",
	"right_pinky_03" :  "f_pinky.03.R",
	"left_shoulder" :  "clavicle.L",
	"left_arm_01" :   "upper_arm.bend.twk.L",
	"left_arm_02" :  "forearm.bend.twk.L",
	"left_hand" :  "hand.twk.L",
	"left_thumb_01" :  "thumb.01.L",
	"left_thumb_02" :  "thumb.02.L",
	"left_thumb_03" :  "thumb.03.L",
	"left_index_01" :  "f_index.01.L",
	"left_index_02" :  "f_index.02.L",
	"left_index_03" :  "f_index.03.L",
	"left_middle_01" :  "f_middle.01.L",
	"left_middle_02" :  "f_middle.02.L",
	"left_middle_03" :  "f_middle.03.L",
	"left_ring_01" :  "f_ring.01.L",
	"left_ring_02" :  "f_ring.02.L",
	"left_ring_03" :  "f_ring.03.L",
	"left_pinky_01" :  "f_pinky.01.L",
	"left_pinky_02" :  "f_pinky.02.L",
	"left_pinky_03" :  "f_pinky.03.L",
	"left_leg_01" :  "thigh.bend.twk.L",
	"left_leg_02" :  "shin.L",
	"left_foot" :  "foot.twk.L",
	"left_toe" :  "toe.L",
	}
	
	
reparent = {
}
	
for rig in bpy.context.selected_objects:
	if rig.type == 'ARMATURE':
		for b in rig.pose.bones:
			if b.name in conversion:
				tempname = b.name
				for mesh in rig.children:
					if tempname in mesh.vertex_groups:
						mesh.vertex_groups[tempname].name = conversion[tempname]
				rig.pose.bones[tempname].name = conversion[tempname]