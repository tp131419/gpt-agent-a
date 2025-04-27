import os
import importlib

def load_plugins(app, plugin_folder="backend.plugins"):
    plugin_path = os.path.join(os.path.dirname(__file__), "plugins")
    for file in os.listdir(plugin_path):
        if file.endswith("_plugin.py"):
            module_name = f"{plugin_folder}.{file[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "register_plugin"):
                module.register_plugin(app)
