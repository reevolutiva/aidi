import importlib
import json
import os
import shutil
from datetime import datetime
import logging
import time

from camel.agents import RolePlaying
from camel.configs import ChatGPTConfig
from camel.typing import TaskType, ModelType
from chatdev.chat_env import ChatEnv, ChatEnvConfig
from chatdev.statistics import get_info
from chatdev.utils import log_and_print_online, now

def check_bool(s):
    return s.lower() == "true"

class ChatChain:
    # ... Rest of the code ...
