"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: print_prompt.py
Description: For printing prompts when the setting for verbose is set to True.
"""
import sys

sys.path.append("../")

import json
import numpy
import datetime
import random

import logging
logger = logging.getLogger(__name__)

from global_methods import *
from persona.prompt_template.gpt_structure import *
from utils import *

##############################################################################
#                    PERSONA Chapter 1: Prompt Structures                    #
##############################################################################


def print_run_prompts(
    prompt_template=None,
    persona=None,
    gpt_param=None,
    prompt_input=None,
    prompt=None,
    output=None,
):
    logger.info(f"=== {prompt_template}")
    logger.info("~~~ persona    ---------------------------------------------------")
    logger.info(persona.name)
    logger.info("~~~ gpt_param ----------------------------------------------------")
    logger.info(gpt_param)
    logger.info("~~~ prompt_input    ----------------------------------------------")
    logger.info(prompt_input)
    logger.info("~~~ prompt    ----------------------------------------------------")
    logger.info(prompt)
    logger.info("~~~ output    ----------------------------------------------------")
    logger.info(output)
    logger.info("=== END ==========================================================")
    logger.info("\n\n\n")
