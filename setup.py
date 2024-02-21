from setuptools import find_packages,setup
from typing import List

#HYPEN_E_DOT='-e .'

def get_requirments(file_path:str)->list[str]:
    
    requirments=[]
    
    with open(file_path) as file_obj:
        requirments=file_obj.readline()
        requirments=[req.replace('/n',"") for req in requirments]
        
        '''if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)'''
        
    return requirments





setup(
    name='Student Performance Indicator',
    version='0.0.1',
    author='vishal chouahan',
    author_email='chouhanvishal6609@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments("Requirment.txt")
)