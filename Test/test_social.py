import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SocialService.SocialRender import SocialRender
from SocialService.Social.LinkedinService import LinkedinService

def test_constructor():
    social = SocialRender("LINKedIN").service

    assert type(social) == LinkedinService

