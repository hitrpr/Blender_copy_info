## Copy Blender Info	######


bl_info = {
	"name": "Blender Info to Clipboard",
	"description": "Copy Build name, hash and date to clipboard. Useful whan you report bugs and want to copy such data for working branch",
	"location": "Help Menu > Copy info",
	"author": "Kobozev Vyacheslav",
	"version": (0, 0, 1),
	"blender": (2, 80, 0),
	"wiki_url": "",
	"tracker_url": "",
	"category": "User"
}

import bpy

from bpy.types import Operator


class CI_OT_CopyInfo(Operator):
	"""Copies Blender info to clipboard"""
	bl_idname="ci.copy_info"
	bl_label="Copy info"

	def execute(self,context):
		version = bpy.app.version_string
		build = bpy.app.build_branch
		comDate = bpy.app.build_commit_date
		comTime = bpy.app.build_commit_time
		buildHash = bpy.app.build_hash
		buildType = bpy.app.build_type

		appInfo = version+", "+buildHash.decode()+", "+comDate.decode()+" "+comTime.decode()
		bpy.context.window_manager.clipboard=appInfo
		self.report({'INFO'}, 'Info copied, ready to paste :)')
		return {'FINISHED'}


def CI_CopyOP(self, context):
	self.layout.operator("ci.copy_info",text="Copy info", icon="COPYDOWN")

classes = (
	CI_OT_CopyInfo
)


def register():
	bpy.utils.register_class(CI_OT_CopyInfo)
	bpy.types.TOPBAR_MT_help.prepend(CI_CopyOP)

def unregister():
	bpy.utils.unregister_class(CI_OT_CopyInfo)
	bpy.types.TOPBAR_MT_help.remove(CI_CopyOP)

if __name__ == "__main__":
	register()
