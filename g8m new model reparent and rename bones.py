import bpy



conversion = {
    "lTesticle" : "Testicle.L",
    "rTesticle" : "Testicle.R",
}

rigname = 'Genesis 8.1 Male' #Default rig name
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
    "Rectum_Open" : "pelvis.twk",
    "Breath" : "chest.twk",
    "Breath.Belly" : "spine-1.twk"
}

arm = bpy.data.objects[rigname]
bpy.ops.object.mode_set(mode='EDIT')
for bone in reparent.keys():
    if arm.data.edit_bones[bone]:
        arm.data.edit_bones[bone].parent = arm.data.edit_bones[reparent[bone]]
        
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