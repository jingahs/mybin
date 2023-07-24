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
    "Vagina_bone_2" : "Genitals",
    "Vagina_bone_1" : "Genitals",
    "Vagina_open" : "Genitals",
    "Rectum_open" : "Anus",
    "Breath" : "chest.twk",
    "Breath.Belly" : "spine-1.twk"
}

arm = bpy.data.objects[rigname]
bpy.ops.object.mode_set(mode='EDIT')
for bone in reparent.keys():
    if arm.data.edit_bones[bone]:
        arm.data.edit_bones[bone].parent = arm.data.edit_bones[reparent[bone]]
    
    #bpy.ops.object.mode_set(mode='POSE')
    #arm.data.pose.bones[bone].custom_shape = bpy.data.objects[]
    
#Bone constraints
bpy.ops.object.mode_set(mode='POSE')
bone = arm.pose.bones.get("chest-1")
if "Copy Location back" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Copy Location back"))
constraint = bone.constraints.new("COPY_LOCATION")
constraint.target = arm
constraint.name = "Copy Location back"
constraint.subtarget = "back"
constraint.influence = 1
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"

bone = arm.pose.bones.get("chest")
if "Copy Location back" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Copy Location back"))
constraint = bone.constraints.new("COPY_LOCATION")
constraint.target = arm
constraint.name = "Copy Location back"
constraint.subtarget = "back"
constraint.influence = 1
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"

bone = arm.pose.bones.get("spine-1")
if "Copy Location back" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Copy Location back"))
constraint = bone.constraints.new("COPY_LOCATION")
constraint.target = arm
constraint.name = "Copy Location back"
constraint.subtarget = "back"
constraint.influence = .5
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"

bone = arm.pose.bones.get("spine")
if "Copy Location back" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Copy Location back"))
constraint = bone.constraints.new("COPY_LOCATION")
constraint.target = arm
constraint.name = "Copy Location back"
constraint.subtarget = "back"
constraint.influence = .25
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"

bone = arm.pose.bones.get("spine-1.twk")
if "Copy Rotation pelvis" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Copy Rotation pelvis"))
constraint = bone.constraints.new("COPY_ROTATION")
constraint.target = arm
constraint.name = "Copy Rotation pelvis"
constraint.subtarget = "pelvis"
constraint.influence = .25
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.invert_y = True
constraint.invert_z = True

bone = arm.pose.bones.get("spine-1.twk")
if "Copy Location pelvis" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Copy Location pelvis"))
constraint = bone.constraints.new("COPY_LOCATION")
constraint.target = arm
constraint.name = "Copy Location pelvis"
constraint.subtarget = "pelvis"
constraint.influence = .25
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.invert_y = True
constraint.invert_z = True

bone = arm.pose.bones.get("spine.twk")
if "Copy Rotation pelvis" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Copy Rotation pelvis"))
constraint = bone.constraints.new("COPY_ROTATION")
constraint.target = arm
constraint.name = "Copy Rotation pelvis"
constraint.subtarget = "pelvis"
constraint.influence = .5
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.invert_y = True
constraint.invert_z = True

bone = arm.pose.bones.get("spine.twk")
if "Copy Location pelvis" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Copy Location pelvis"))
constraint = bone.constraints.new("COPY_LOCATION")
constraint.target = arm
constraint.name = "Copy Location pelvis"
constraint.subtarget = "pelvis"
constraint.influence = .5
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.invert_y = True
constraint.invert_z = True

#Unlock bone axis
bone = arm.pose.bones.get("back")
bone.lock_location[0] = False
bone.lock_location[1] = False
bone.lock_location[2] = False

bone = arm.pose.bones.get("pelvis")
bone.lock_location[0] = False
bone.lock_location[1] = False
bone.lock_location[2] = False

#Breath
bone = arm.pose.bones.get("chest.twk")
if "Breath Control 1" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Breath Control 1"))
constraint = bone.constraints.new("TRANSFORM")
constraint.target = arm
constraint.name = "Breath Control 1"
constraint.subtarget = "Breath"
constraint.influence = .8
constraint.use_motion_extrapolate = True
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.from_min_y = -.5
constraint.from_max_y = .5
constraint.map_to = "SCALE"
constraint.map_to_x_from = "Y"
constraint.map_to_y_from = "Y"
constraint.map_to_z_from = "Y"
constraint.to_min_x_scale = 0
constraint.to_max_x_scale = 2
constraint.to_min_y_scale = 0
constraint.to_max_y_scale = 2
constraint.to_min_z_scale = 0
constraint.to_max_z_scale = 2

if "Breath Control 2" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Breath Control 2"))
constraint = bone.constraints.new("TRANSFORM")
constraint.target = arm
constraint.name = "Breath Control 2"
constraint.subtarget = "Breath"
constraint.influence = .2
constraint.use_motion_extrapolate = True
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.from_min_x = -1
constraint.from_max_x = 1
constraint.from_min_y = -1
constraint.from_max_y = 1
constraint.map_to_x_from = "X"
constraint.map_to_y_from = "Y"
constraint.map_to_z_from = "Y"
constraint.to_min_x = -1
constraint.to_max_x = 1
constraint.to_min_y = -1
constraint.to_max_y = 1
constraint.to_min_z = -1
constraint.to_max_z = 1
constraint.mix_mode = "ADD"

bone = arm.pose.bones.get("spine-1.twk")
if "Breath Control 1" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Breath Control 1"))
constraint = bone.constraints.new("TRANSFORM")
constraint.target = arm
constraint.name = "Breath Control 1"
constraint.subtarget = "Breath"
constraint.influence = .8
constraint.use_motion_extrapolate = True
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.from_min_y = -.5
constraint.from_max_y = .5
constraint.map_to = "SCALE"
constraint.map_to_x_from = "Y"
constraint.map_to_y_from = "Y"
constraint.map_to_z_from = "Y"
constraint.to_min_x_scale = 0
constraint.to_max_x_scale = 2
constraint.to_min_y_scale = 0
constraint.to_max_y_scale = 2
constraint.to_min_z_scale = 0
constraint.to_max_z_scale = 2

if "Breath Control 2" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Breath Control 2"))
constraint = bone.constraints.new("TRANSFORM")
constraint.target = arm
constraint.name = "Breath Control 2"
constraint.subtarget = "Breath"
constraint.influence = .3
constraint.use_motion_extrapolate = True
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.from_min_x = -1
constraint.from_max_x = 1
constraint.from_min_y = -1
constraint.from_max_y = 1
constraint.from_min_z = -1
constraint.from_max_z = 1
constraint.to_min_x = -1
constraint.to_max_x = 1
constraint.to_min_y = -1
constraint.to_max_y = 1
constraint.to_min_z = -1
constraint.to_max_z = 1
constraint.mix_mode = "ADD"

bone = arm.pose.bones.get("spine.twk")
if "Breath Control 1" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Breath Control 1"))
constraint = bone.constraints.new("TRANSFORM")
constraint.target = arm
constraint.name = "Breath Control 1"
constraint.subtarget = "Breath"
constraint.influence = 1
constraint.use_motion_extrapolate = True
constraint.owner_space = "LOCAL"
constraint.target_space = "LOCAL"
constraint.from_min_y = -.5
constraint.from_max_y = .5
constraint.map_to = "SCALE"
constraint.map_to_x_from = "Y"
constraint.map_to_y_from = "Y"
constraint.map_to_z_from = "Y"
constraint.to_min_x_scale = 1
constraint.to_max_x_scale = 1
constraint.to_min_y_scale = 1
constraint.to_max_y_scale = 1
constraint.to_min_z_scale = 1
constraint.to_max_z_scale = 1

bone = arm.pose.bones.get("Breath")
if "Limit Location" in bone.constraints:
    bone.constraints.remove(bone.constraints.get("Limit Location"))
constraint = bone.constraints.new("LIMIT_LOCATION")
constraint.min_y = -0.05
constraint.max_y = 0.05
constraint.use_min_y = True
constraint.use_max_y = True
constraint.owner_space = "LOCAL"
bone.lock_location[1] = False