# Stubs for galaxy.tools.parser.yaml (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .interface import InputSource as InputSource
from .interface import PageSource as PageSource
from .interface import PagesSource as PagesSource
from .interface import ToolSource as ToolSource
from .output_actions import ToolOutputActionGroup as ToolOutputActionGroup
from .output_collection_def import dataset_collector_descriptions_from_list as dataset_collector_descriptions_from_list
from .output_objects import ToolOutput as ToolOutput, ToolOutputCollection as ToolOutputCollection, ToolOutputCollectionStructure as ToolOutputCollectionStructure
from .util import error_on_exit_code as error_on_exit_code

class YamlToolSource(ToolSource):
    root_dict = ...  # type: Any
    def __init__(self, root_dict, source_path: Optional[Any] = ...) -> None: ...
    def parse_id(self): ...
    def parse_version(self): ...
    def parse_name(self): ...
    def parse_description(self): ...
    def parse_edam_operations(self): ...
    def parse_edam_topics(self): ...
    def parse_is_multi_byte(self): ...
    def parse_sanitize(self): ...
    def parse_display_interface(self, default): ...
    def parse_require_login(self, default): ...
    def parse_command(self): ...
    def parse_environment_variables(self): ...
    def parse_interpreter(self): ...
    def parse_version_command(self): ...
    def parse_version_command_interpreter(self): ...
    def parse_requirements_and_containers(self): ...
    def parse_input_pages(self): ...
    def parse_strict_shell(self): ...
    def parse_stdio(self): ...
    def parse_help(self): ...
    def parse_outputs(self, tool): ...
    def parse_tests_to_dict(self): ...
    def parse_profile(self): ...

class YamlPageSource(PageSource):
    inputs_list = ...  # type: Any
    def __init__(self, inputs_list) -> None: ...
    def parse_input_sources(self): ...

class YamlInputSource(InputSource):
    input_dict = ...  # type: Any
    def __init__(self, input_dict) -> None: ...
    def get(self, key, default: Optional[Any] = ...): ...
    def get_bool(self, key, default): ...
    def parse_input_type(self): ...
    def parse_nested_inputs_source(self): ...
    def parse_test_input_source(self): ...
    def parse_when_input_sources(self): ...
    def parse_static_options(self): ...
