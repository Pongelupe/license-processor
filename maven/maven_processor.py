#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys

path_pom = sys.argv[1] # path to maven xml

dependencies = []

root = ET.parse(path_pom).getroot()
for el in root:
    if 'dependencies' in el.tag:
        for d in el:
            dependency = {'groupId': '', 'artifactId': '' }
            dependencies.append(dependency)
            for i in d:
                if 'groupId' in i.tag:
                    dependency['groupId'] = i.text
                elif 'artifactId' in i.tag:
                    dependency['artifactId'] = i.text

print(dependencies)
