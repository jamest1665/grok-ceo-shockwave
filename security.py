import docker
from config import config

class ZeroTrustPolicy:
    def check(self, action, ctx):
        if config.DRY_RUN and 'git:write' in action:
            print('🚨 DRY RUN BLOCKED')
            return False
        return True

policy = ZeroTrustPolicy()