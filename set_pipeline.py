import yaml
import json

filename = './creds.yml'

resources_template = """
---
resources:
- name: git_docker_image
  type: git
  tags: [public]
  source:
    uri: https://github.com/lee-andrew/dockerhub-images.git 

"""

jobs_template = """
jobs:
- name: Reapply Docker Image
  plan:
  - get: git_docker_image
    tags: [public]
    trigger: true
  - task: apply_pipeline
    tags: [public]
    file: git_docker_image/tasks/apply_pipeline/task.yml
    params: {}
"""

with open(filename, 'r') as stream:
    try:
        creds = yaml.load(stream)
        resources = yaml.load(resources_template)
        jobs = yaml.load(jobs_template)
	for job in jobs["jobs"]:
          plan = job["plan"]
          for p in plan:
            if "task" in p and "params" in p:
              params = p["params"]
              params["creds"] = creds
              params["concourse_host"] = creds["concourse_host"]
              params["concourse_username"] = creds["concourse_username"]
              params["concourse_password"] = creds["concourse_password"]
        resources["jobs"] = jobs["jobs"]
        print(json.dumps(resources))
    except yaml.YAMLError as exc:
        print(exc)
