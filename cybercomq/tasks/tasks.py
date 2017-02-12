from celery.task import task
from dockertask import docker_task
from subprocess import call,STDOUT
import requests

#Default base directory 
#basedir="/data/static/"


#Example task
@task()
def add(x, y,cybercom_auth_token=None):
    """ Example task that adds two numbers or strings
        args: x and y
        kwargs: cybercom_auth_token (Default add by cybercommons)
        return addition or concatination of strings
    """
    result = x + y
    if cybercom_auth_token:
        return cybercom_auth_token
    return result
@task()
def subtract(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x - y
    return result
