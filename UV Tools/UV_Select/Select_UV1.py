import bpy


for ob in bpy.context.selected_objects:
        bpy.context.scene.objects.active = ob
        mesh = bpy.context.active_object.data
        if len(mesh.uv_textures.items()) >= 2:
                mesh.uv_textures.active_index = 1
bpy.ops.hops.draw_uv()
