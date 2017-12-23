from os import listdir
from os.path import isdir

def hasDockerfile (directory):
  for x in listdir(directory):
    if x == 'Dockerfile':
      return True
  return False

dockerfiles = [x for x in listdir('.') if isdir(x) and hasDockerfile(x) ]

resources = "resources:\n"
resource_template = """
- name: %(dockerfile)s-image-repo
  type: git
  tags: [public]
  source:
    uri: https://github.com/lee-andrew/dockerhub-images.git
    branch: master
    paths:
    - %(dockerfile)s

- name: %(dockerfile)s-dockerfile
  type: docker-image
  tags: [public] 
  source:
    repository: ((docker_account))/privatebox
    username: ((docker_username))
    password: ((docker_password))
"""

jobs = "jobs:\n"
job_template = """
- name: %(dockerfile)s
  plan:
  - get: %(dockerfile)s-image-repo
    trigger: true
    tags: [public] 
  - put: %(dockerfile)s-dockerfile
    params: {build: %(dockerfile)s-image-repo/%(dockerfile)s}
    tags: [public] 
"""


for dockerfile in dockerfiles:
  resources = resources + resource_template % {"dockerfile": dockerfile}
  jobs = jobs + job_template % {"dockerfile": dockerfile}

print(resources + jobs)
