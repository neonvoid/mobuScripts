
from pyfbsdk import *
import os 
import xml.etree.ElementTree as etree

def getCharacterXML(fileName):
    xmlFilePath = os.path.join(os.path.expanduser('~'), "AppData","Roaming","Autodesk","HIKCharacterizationTool6","template",fileName)

    parsedXML = etree.parse(xmlFilePath)

    xmlDict = {}

    for line in parsedXML.iter('item'):
        jointName = line.attrib.get('value')
        if jointName:
            slotName = line.attrib.get('key')
            xmlDict[slotName] = jointName
    return xmlDict
    

parts = []
def CollectParts(part_name):
    part = JointNames.get(part_name)
    obj = FBFindModelByLabelName(part)
    parts.append(obj)

JointNames = getCharacterXML('TravisSkeleton.xml')
CollectParts('Hips')
CollectParts('Head')
CollectParts('RightHand')
CollectParts('LeftHand')
CollectParts('LeftFoot')
CollectParts('RightFoot')

def spawnCube():
    for p in parts:
        cube = FBModelCube("cube")
        cube.Show = True
        cube.Scaling = FBVector3d(5,5,5)
        vector = FBVector3d()
        p.GetVector(vector,FBModelTransformationType.kModelTranslation, True)
        cube.SetVector(vector,FBModelTransformationType.kModelTranslation, True)
        cube.Parent = p

spawnCube()