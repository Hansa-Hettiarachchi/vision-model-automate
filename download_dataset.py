from roboflow import Roboflow

rf = Roboflow(api_key="FMJblBkjpLkjWDc3Sr3N")
project = rf.workspace("fyp-fqnbg").project("socket_detection")
dataset = project.version(4).download("yolov8")
