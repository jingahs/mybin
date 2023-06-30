import bpy


baseKeys = {
    "battle_00_m4_face_mesh_shape" : ["battle_00_m4_eyebrow_mesh_shape"],
    "battle_00_m3_face_mesh_shape" : ["battle_00_m3_eyelash_mesh_shape"],
    "battle_00_m2_face_mesh_shape" : ["battle_00_m2_eyelash_mesh_shape"],
    "battle_00_m1_face_mesh_shape" : ["battle_00_m1_tooth_mesh_shape", "battle_00_m1_tongue_mesh_shape"],
    "battle_01_m3_face_mesh_shape" : ["battle_01_m3_eyelash_mesh_shape",],
    "battle_01_m2_face_mesh_shape" : ["battle_01_m2_eyelash_mesh_shape"],
    "battle_01_m1_face_mesh_shape" : ["battle_01_m1_tongue_mesh_shape","battle_01_m1_tooth_mesh_shape"],
    "add_bend_l_m1_face_mesh_shape" : ["add_bend_l_m1_tongue_mesh_shape","add_bend_l_m1_tooth_mesh_shape"],
    "add_bend_l_m2_face_mesh_shape" : ["add_bend_l_m2_eyelash_mesh_shape",],
    "add_bend_l_m3_face_mesh_shape" : ["add_bend_l_m3_eyelash_mesh_shape"],
    "add_bend_r_m3_face_mesh_shape" : ["add_bend_r_m3_eyelash_mesh_shape",],
    "add_bend_r_m2_face_mesh_shape" : ["add_bend_r_m2_eyelash_mesh_shape"],
    "add_bend_r_m1_face_mesh_shape" : ["add_bend_r_m1_tongue_mesh_shape","add_bend_r_m1_tooth_mesh_shape"],
    "add_mtn_00_m1_face_mesh_shape" : ["add_mtn_00_m1_tongue_mesh_shape","add_mtn_00_m1_tooth_mesh_shape"],
    "add_mtn_00_m2_face_mesh_shape" : ["add_mtn_00_m2_eyelash_mesh_shape"],
    "add_mtn_00_m3_face_mesh_shape" : ["add_mtn_00_m3_eyelash_mesh_shape"],
    "add_mtn_01_m1_face_mesh_shape" : ["add_mtn_01_m1_tongue_mesh_shape","add_mtn_01_m1_tooth_mesh_shape"],
    "add_mtn_01_m2_face_mesh_shape" : ["add_mtn_01_m2_eyelash_mesh_shape"],
    "add_mtn_01_m3_face_mesh_shape" : ["add_mtn_01_m3_eyelash_mesh_shape"],
    "add_smile_m1_face_mesh_shape" : ["add_smile_m1_tongue_mesh_shape","add_smile_m1_tooth_mesh_shape"],
    "add_smile_m2_face_mesh_shape" : ["add_smile_m2_eyelash_mesh_shape"],
    "add_smile_m3_face_mesh_shape" : ["add_smile_m3_eyelash_mesh_shape"],
    "bendeb_l_m4_face_mesh_shape" : ["bendeb_l_m4_eyebrow_mesh_shape"],
    "bendeb_r_m4_face_mesh_shape" : ["bendeb_r_m4_eyebrow_mesh_shape"],
    "down_m1_face_mesh_shape" : ["down_m1_tongue_mesh_shape","down_m1_tooth_mesh_shape"],
    "down_m2_face_mesh_shape" : ["down_m2_eyelash_mesh_shape"],
    "down_m3_face_mesh_shape" : ["down_m3_eyelash_mesh_shape"],
    "down_m4_face_mesh_shape" : ["down_m4_eyebrow_mesh_shape"],
    "eye_close_m2_face_mesh_shape" : ["eye_close_m2_eyelash_mesh_shape"],
    "eye_close_m3_face_mesh_shape" : ["eye_close_m3_eyelash_mesh_shape"],
    "eye_strong_close_m2_face_mesh_shape" : ["eye_strong_close_m2_eyelash_mesh_shape"],
    "eye_strong_close_m3_face_mesh_shape" : ["eye_strong_close_m3_eyelash_mesh_shape"],
    "mouth_a_m1_face_mesh_shape" : ["mouth_a_m1_tongue_mesh_shape","mouth_a_m1_tooth_mesh_shape"],
    "mouth_i_m1_face_mesh_shape" : ["mouth_i_m1_tongue_mesh_shape","mouth_i_m1_tooth_mesh_shape"],
    "mouth_o_m1_face_mesh_shape" : ["mouth_o_m1_tongue_mesh_shape","mouth_o_m1_tooth_mesh_shape"],
    "mouth_u_m1_face_mesh_shape" : ["mouth_u_m1_tongue_mesh_shape","mouth_u_m1_tooth_mesh_shape"],
    "serious_m4_face_mesh_shape" : ["serious_m4_eyebrow_mesh_shape"],
    "unique_00_m1_face_mesh_shape" : ["unique_00_m1_tongue_mesh_shape","unique_00_m1_tooth_mesh_shape"],
    "unique_00_m2_face_mesh_shape" : ["unique_00_m2_eyelash_mesh_shape"],
    "unique_00_m3_face_mesh_shape" : ["unique_00_m3_eyelash_mesh_shape"],
    "unique_00_m4_face_mesh_shape" : ["unique_00_m4_eyebrow_mesh_shape"],
    "unique_01_m1_face_mesh_shape" : ["unique_01_m1_tongue_mesh_shape","unique_01_m1_tooth_mesh_shape"],
    "unique_01_m2_face_mesh_shape" : ["unique_01_m2_eyelash_mesh_shape"],
    "unique_01_m3_face_mesh_shape" : ["unique_01_m3_eyelash_mesh_shape"],
    "unique_01_m4_face_mesh_shape" : ["unique_01_m4_eyebrow_mesh_shape"],
    "unique_02_m1_face_mesh_shape" : ["unique_02_m1_tongue_mesh_shape","unique_02_m1_tooth_mesh_shape"],
    "unique_02_m2_face_mesh_shape" : ["unique_02_m2_eyelash_mesh_shape"],
    "unique_02_m3_face_mesh_shape" : ["unique_02_m3_eyelash_mesh_shape"],
    "unique_02_m4_face_mesh_shape" : ["unique_02_m4_eyebrow_mesh_shape"],
    "unique_03_m1_face_mesh_shape" : ["unique_03_m1_tongue_mesh_shape","unique_03_m1_tooth_mesh_shape"],
    "unique_03_m2_face_mesh_shape" : ["unique_03_m2_eyelash_mesh_shape"],
    "unique_03_m3_face_mesh_shape" : ["unique_03_m3_eyelash_mesh_shape"],
    "unique_03_m4_face_mesh_shape" : ["unique_03_m4_eyebrow_mesh_shape"],
    "unique_04_m2_face_mesh_shape" : ["unique_04_m2_eyelash_mesh_shape"],
    "unique_04_m3_face_mesh_shape" : ["unique_04_m3_eyelash_mesh_shape"],
    "up_m1_face_mesh_shape" : ["up_m1_tongue_mesh_shape","up_m1_tooth_mesh_shape"],
    "up_m4_face_mesh_shape" : ["up_m4_eyebrow_mesh_shape"],
	"battle_01_m4_face_mesh_shape" : ["battle_01_m4_eyebrow_mesh_shape"],
}

curr_obj = bpy.context.active_object

#Get the list of the object's keys to see if they have them
object_keys = []
for key in curr_obj.data.shape_keys.key_blocks:
    object_keys.append(key.name)


#Go through the dict's keys, then get their array data
#Add a driver to each array index with the dict key as the source of the driver
for key in list(baseKeys.keys()):
    if key in object_keys:
        for subkey in baseKeys.get(key):
            if subkey in object_keys:
                #sample : new_driver = curr_obj.data.shape_keys.key_blocks['unique_00_m4_eyebrow_mesh_shape'].driver_add("value")
                new_driver = curr_obj.data.shape_keys.key_blocks[subkey].driver_add("value")
                new_driver.driver.type = 'AVERAGE'
                
                #Remove variables if they exist (they aren't deleted if driver is replaced)
                if new_driver.driver.variables:
                    for v in new_driver.driver.variables:
                        new_driver.driver.variables.remove(v)
                
                newVar = new_driver.driver.variables.new()
                newVar.name = "var"
                newVar.type = 'SINGLE_PROP'
                newVar.targets[0].id_type = 'MESH'
                newVar.targets[0].id = curr_obj.data
                newVar.targets[0].data_path = 'shape_keys.key_blocks["' + key + '"].value'

"""
List of keys
add_bend_l_m1_face_mesh_shape
add_bend_l_m1_tongue_mesh_shape
add_bend_l_m1_tooth_mesh_shape
add_bend_l_m2_eyelash_mesh_shape
add_bend_l_m2_face_mesh_shape
add_bend_l_m3_eyelash_mesh_shape
add_bend_l_m3_face_mesh_shape
add_bend_l_m4_face_mesh_shape
add_bend_r_m1_face_mesh_shape
add_bend_r_m1_tongue_mesh_shape
add_bend_r_m1_tooth_mesh_shape
add_bend_r_m2_eyelash_mesh_shape
add_bend_r_m2_face_mesh_shape
add_bend_r_m3_eyelash_mesh_shape
add_bend_r_m3_face_mesh_shape
add_bend_r_m4_face_mesh_shape
add_mtn_00_m1_face_mesh_shape
add_mtn_00_m1_tongue_mesh_shape
add_mtn_00_m1_tooth_mesh_shape
add_mtn_00_m2_eyelash_mesh_shape
add_mtn_00_m2_face_mesh_shape
add_mtn_00_m3_eyelash_mesh_shape
add_mtn_00_m3_face_mesh_shape
add_mtn_00_m4_face_mesh_shape
add_mtn_01_m1_face_mesh_shape
add_mtn_01_m1_tongue_mesh_shape
add_mtn_01_m1_tooth_mesh_shape
add_mtn_01_m2_eyelash_mesh_shape
add_mtn_01_m2_face_mesh_shape
add_mtn_01_m3_eyelash_mesh_shape
add_mtn_01_m3_face_mesh_shape
add_mtn_01_m4_face_mesh_shape
add_smile_m1_face_mesh_shape
add_smile_m1_tongue_mesh_shape
add_smile_m1_tooth_mesh_shape
add_smile_m2_eyelash_mesh_shape
add_smile_m2_face_mesh_shape
add_smile_m3_eyelash_mesh_shape
add_smile_m3_face_mesh_shape
add_smile_m4_face_mesh_shape
battle_00_m1_face_mesh_shape
battle_00_m1_tongue_mesh_shape
battle_00_m1_tooth_mesh_shape
battle_00_m2_eyelash_mesh_shape
battle_00_m2_face_mesh_shape
battle_00_m3_eyelash_mesh_shape
battle_00_m3_face_mesh_shape
battle_00_m4_eyebrow_mesh_shape
battle_01_m1_face_mesh_shape
battle_01_m1_tongue_mesh_shape
battle_01_m1_tooth_mesh_shape
battle_01_m2_eyelash_mesh_shape
battle_01_m2_face_mesh_shape
battle_01_m3_eyelash_mesh_shape
battle_01_m3_face_mesh_shape
battle_01_m4_eyebrow_mesh_shape
battle_01_m4_face_mesh_shape
bendeb_l_m4_eyebrow_mesh_shape
bendeb_l_m4_face_mesh_shape
bendeb_r_m4_eyebrow_mesh_shape
bendeb_r_m4_face_mesh_shape
down_m1_face_mesh_shape
down_m1_tongue_mesh_shape
down_m1_tooth_mesh_shape
down_m2_eyelash_mesh_shape
down_m2_face_mesh_shape
down_m3_eyelash_mesh_shape
down_m3_face_mesh_shape
down_m4_eyebrow_mesh_shape
down_m4_face_mesh_shape
eye_close_m2_eyelash_mesh_shape
eye_close_m2_face_mesh_shape
eye_close_m3_eyelash_mesh_shape
eye_close_m3_face_mesh_shape
eye_strong_close_m2_eyelash_mesh_shape
eye_strong_close_m2_face_mesh_shape
eye_strong_close_m3_eyelash_mesh_shape
eye_strong_close_m3_face_mesh_shape
mouth_a_m1_face_mesh_shape
mouth_a_m1_tongue_mesh_shape
mouth_a_m1_tooth_mesh_shape
mouth_i_m1_face_mesh_shape
mouth_i_m1_tongue_mesh_shape
mouth_i_m1_tooth_mesh_shape
mouth_o_m1_face_mesh_shape
mouth_o_m1_tongue_mesh_shape
mouth_o_m1_tooth_mesh_shape
mouth_u_m1_face_mesh_shape
mouth_u_m1_tongue_mesh_shape
mouth_u_m1_tooth_mesh_shape
serious_m4_eyebrow_mesh_shape
serious_m4_face_mesh_shape
unique_00_m1_face_mesh_shape
unique_00_m1_tongue_mesh_shape
unique_00_m1_tooth_mesh_shape
unique_00_m2_eyelash_mesh_shape
unique_00_m2_face_mesh_shape
unique_00_m3_eyelash_mesh_shape
unique_00_m3_face_mesh_shape
unique_00_m4_eyebrow_mesh_shape
unique_00_m4_face_mesh_shape
unique_01_m1_face_mesh_shape
unique_01_m1_tongue_mesh_shape
unique_01_m1_tooth_mesh_shape
unique_01_m2_eyelash_mesh_shape
unique_01_m2_face_mesh_shape
unique_01_m3_eyelash_mesh_shape
unique_01_m3_face_mesh_shape
unique_01_m4_eyebrow_mesh_shape
unique_01_m4_face_mesh_shape
unique_02_m1_face_mesh_shape
unique_02_m1_tongue_mesh_shape
unique_02_m1_tooth_mesh_shape
unique_02_m2_eyelash_mesh_shape
unique_02_m2_face_mesh_shape
unique_02_m3_eyelash_mesh_shape
unique_02_m3_face_mesh_shape
unique_02_m4_eyebrow_mesh_shape
unique_02_m4_face_mesh_shape
unique_03_m1_face_mesh_shape
unique_03_m1_tongue_mesh_shape
unique_03_m1_tooth_mesh_shape
unique_03_m2_eyelash_mesh_shape
unique_03_m2_face_mesh_shape
unique_03_m3_eyelash_mesh_shape
unique_03_m3_face_mesh_shape
unique_03_m4_eyebrow_mesh_shape
unique_03_m4_face_mesh_shape
unique_04_m2_eyelash_mesh_shape
unique_04_m2_face_mesh_shape
unique_04_m3_eyelash_mesh_shape
unique_04_m3_face_mesh_shape
up_m1_face_mesh_shape
up_m1_tongue_mesh_shape
up_m1_tooth_mesh_shape
up_m4_eyebrow_mesh_shape
up_m4_face_mesh_shape

battle_00_m3_tears_mesh_shape
battle_01_m3_tears_mesh_shape
unique_00_m3_tears_mesh_shape
unique_01_m3_tears_mesh_shape
unique_02_m3_tears_mesh_shape
unique_03_m3_tears_mesh_shape
unique_04_m3_tears_mesh_shape
eye_close_m3_tears_mesh_shape
add_smile_m3_tears_mesh_shape
add_bend_l_m3_tears_mesh_shape
add_bend_r_m3_tears_mesh_shape
down_m3_tears_mesh_shape
eye_strong_close_m3_tears_mesh_shape
add_mtn_00_m3_tears_mesh_shape
add_mtn_01_m3_tears_mesh_shape
battle_00_m2_tears_mesh_shape
battle_01_m2_tears_mesh_shape
unique_00_m2_tears_mesh_shape
unique_01_m2_tears_mesh_shape
unique_02_m2_tears_mesh_shape
unique_03_m2_tears_mesh_shape
unique_04_m2_tears_mesh_shape
eye_close_m2_tears_mesh_shape
add_smile_m2_tears_mesh_shape
add_bend_l_m2_tears_mesh_shape
add_bend_r_m2_tears_mesh_shape
down_m2_tears_mesh_shape
eye_strong_close_m2_tears_mesh_shape
add_mtn_00_m2_tears_mesh_shape
add_mtn_01_m2_tears_mesh_shape

"""