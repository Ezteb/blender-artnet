import bpy

class LightArtNetPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_light_artnet"
    bl_label = "ArtNet Light Control"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    #bl_options = {}

    @classmethod
    def poll(cls, context):
        """Only show panel for light objects"""
        return context.object.type == 'LIGHT'

    def draw_header(self, context):
        layout = self.layout
        data = context.object.data
        layout.prop(data, "artnet_enabled", text="")

    def draw(self, context):
        data = context.object.data
        enabled = data.artnet_enabled
        if not enabled:
            return

        layout = self.layout
        layout.prop(data, "artnet_fixture_type", text="Fixture Type")
        layout.prop(data, "artnet_universe", text="Universe")
        layout.prop(data, "artnet_base_address", text="Base DMX Address")
