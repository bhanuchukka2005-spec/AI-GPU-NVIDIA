# pip install inference-sdk
# !pip install roboflow

from inference_sdk import InferenceHTTPClient
from roboflow import Roboflow

rf = Roboflow(api_key="Your API Key")

print(rf.workspace())

from roboflow import Roboflow

rf = Roboflow(api_key="your api")

workspace = rf.workspace("your workspace")

project = workspace.project("project")

model = project.version(1).model

result = model.predict("sample iamge").json()

print(result)