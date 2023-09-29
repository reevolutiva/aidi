# Documentation

This documentation covers the classes in the `chatdev\chat_env.py` file.

## Class: ChatEnvConfig

This class is used to configure the chat environment. It has the following attributes:

- `clear_structure`: (type: bool) 
- `brainstorming`: (type: bool)
- `gui_design`: (type: bool)
- `git_management`: (type: bool)

## Class: ChatEnv

This class represents the chat environment. It has the following attributes:

- `config`: (type: ChatEnvConfig) The configuration for the chat environment.
- `roster`: (type: Roster) The roster of agents.
- `codes`: (type: Codes) The codes used in the environment.
- `proposed_images`: (type: Dict[str, str]) The proposed images for the environment.
- `incorporated_images`: (type: Dict[str, str]) The incorporated images in the environment.
- `requirements`: (type: Documents) The requirements for the environment.
- `manuals`: (type: Documents) The manuals for the environment.
- `env_dict`: (type: dict) The dictionary representing the environment.

This class also has several methods for managing the environment, such as `set_directory`, `exist_bugs`, `recruit`, `exist_employee`, `print_employees`, `update_codes`, `rewrite_codes`, `get_codes`, `_load_from_hardware`, `_update_requirements`, `rewrite_requirements`, `get_requirements`, `_update_manuals`, `rewrite_manuals`, `write_meta`, `generate_images_from_codes`, and `get_proposed_images_from_message`.
