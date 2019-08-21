#!/usr/bin/env python
#
# Copyright (C) 2018 DANS - Data Archiving and Networked Services (info@dans.knaw.nl)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import os, sys, functions

def print_usage():
    print "Emulates a mvn deploy to deploy an RPM to a Nexus Yum repository:"
    print "1. Builds the snapshot"
    print "2. Uploads the resulting SNAPSHOT RPM to the Nexus Yum repository"
    print "Usage: ./deploy-snapshot-rpm.py <nexus_account> <nexus_password> <repo-url> <build_dir>"


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print_usage()
        exit(1)

    nexus_account = sys.argv[1]
    nexus_password = sys.argv[2]
    repo_url = sys.argv[3]
    build_dir = sys.argv[4]

    # Note: this will delete this script, but it will stay in memory to finish execution
    exitStatus = os.system('mvn -f %s/.. clean install' % build_dir)
    if exitStatus != 0:
        print "Maven build failed with exit status: %s" % exitStatus
        exit(2)
    else:
        print "SNAPSHOT successfully built. Deploying to Yum..."
        functions.deploy_rpm(nexus_account, nexus_password, repo_url, build_dir)

