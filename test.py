#!/usr/bin/env python3
"""
"""
import os
from fontTools.ttLib import TTFont
from diffenator import ninja_proof, ninja_diff

ttFonts = [TTFont("ofl/mavenpro/MavenPro[wght].ttf")]
ninja_proof(ttFonts, out="out", imgs=True)