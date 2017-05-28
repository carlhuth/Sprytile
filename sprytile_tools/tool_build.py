import bpy


class ToolBuild:
    def __init__(self, rx_source):
        rx_source.filter(
            lambda x: x.data.paint_mode == 'MAKE_FACE'
        ).subscribe(
            on_next=lambda x: self.process_tool(x),
            on_error=lambda err: self.handle_error(err),
            on_completed=lambda: self.handle_complete()
        )

    def process_tool(self, modal):
        print("Duck season {0}".format(modal.data.paint_mode))
        pass

    def handle_error(self, err):
        pass

    def handle_complete(self):
        pass


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == '__main__':
    register()