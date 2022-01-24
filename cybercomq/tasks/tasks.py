from celery.task import task

#Default base directory 
#basedir="/data/static/"

#Echo task
@task()
def echo(txt):
     """ Echo task that print out the string input
         args: txt
     """
    print(txt)
    return 0	    

#Example task
@task()
def add(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x + y
    return result
