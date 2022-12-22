import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from ch.inss.jwserver.models.error_model import ErrorModel  # noqa: E501
from ch.inss.jwserver.models.metadata import Metadata  # noqa: E501
from ch.inss.jwserver.models.resources import Resources  # noqa: E501
from ch.inss.jwserver.models.shell import Shell  # noqa: E501
from ch.inss.jwserver.models.task import Task  # noqa: E501
from ch.inss.jwserver import util


def add_metadata(metadata):  # noqa: E501
    """Creates new metadata

    Creates new metadata. # noqa: E501

    :param metadata: Metadata to be created
    :type metadata: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        metadata = Metadata.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_resources(filestream, filename=None):  # noqa: E501
    """Creates new resources

    Creates new resources. # noqa: E501

    :param filestream: 
    :type filestream: str
    :param filename: Any file that is needed by a task. Can be a mustache file.
    :type filename: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def add_shell(filestream, filename=None):  # noqa: E501
    """Creates new shell

    Creates new shell. # noqa: E501

    :param filestream: 
    :type filestream: str
    :param filename: Any shell script to execute a task.
    :type filename: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if filename is None:
        filename = '../shell/newunnamedscript.sh'
    else:
        filename = '../shell/' + filename

    filestream.save(filename,512)
    return 'Script created.'


def add_task(task):  # noqa: E501
    """Creates new task

    Creates new task. # noqa: E501

    :param task: Task to be created
    :type task: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        task = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_metadata(name):  # noqa: E501
    """Deletes metadata by name

    Deletes metadata by name. # noqa: E501

    :param name: ID of metadata to delete
    :type name: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_resources(name):  # noqa: E501
    """Deletes resources by name

    Deletes resources by name. # noqa: E501

    :param name: ID of resources to delete
    :type name: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_shell(name):  # noqa: E501
    """Deletes shell by name

    Deletes shell by name. # noqa: E501

    :param name: ID of shell to delete
    :type name: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_task(name):  # noqa: E501
    """Deletes task by name

    Deletes task by name. # noqa: E501

    :param name: ID of task to delete
    :type name: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_metadata_byname(name):  # noqa: E501
    """Returns metadata by name

    Returns metadata by name. # noqa: E501

    :param name: name of metadata to fetch
    :type name: str

    :rtype: Union[Metadata, Tuple[Metadata, int], Tuple[Metadata, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_resources_byname(name):  # noqa: E501
    """Returns resources by name

    Returns resources by name. # noqa: E501

    :param name: name of resources to fetch
    :type name: str

    :rtype: Union[Resources, Tuple[Resources, int], Tuple[Resources, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_shell_byname(name):  # noqa: E501
    """Returns shell by name

    Returns shell by name. # noqa: E501

    :param name: name of shell to fetch
    :type name: str

    :rtype: Union[Shell, Tuple[Shell, int], Tuple[Shell, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_task_byname(name):  # noqa: E501
    """Returns task by name

    Returns task by name. # noqa: E501

    :param name: name of task to fetch
    :type name: str

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_metadata_list():  # noqa: E501
    """List of metadatas

    List of metadatas. # noqa: E501


    :rtype: Union[List[Metadata], Tuple[List[Metadata], int], Tuple[List[Metadata], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_resources_list():  # noqa: E501
    """List of resourcess

    List of resourcess. # noqa: E501


    :rtype: Union[List[Resources], Tuple[List[Resources], int], Tuple[List[Resources], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_shell_list():  # noqa: E501
    """List of shells

    List of shells. # noqa: E501


    :rtype: Union[List[Shell], Tuple[List[Shell], int], Tuple[List[Shell], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_task_list():  # noqa: E501
    """List of tasks

    List of tasks. # noqa: E501


    :rtype: Union[List[Task], Tuple[List[Task], int], Tuple[List[Task], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_metadata(name, metadata):  # noqa: E501
    """Updates metadata by name

    Updates metadata by name. # noqa: E501

    :param name: ID of metadata to put
    :type name: str
    :param metadata: Metadata to be updated
    :type metadata: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        metadata = Metadata.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_resources(name, resources):  # noqa: E501
    """Updates resources by name

    Updates resources by name. # noqa: E501

    :param name: ID of resources to put
    :type name: str
    :param resources: Resources to be updated
    :type resources: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        resources = Resources.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_shell(name, shell):  # noqa: E501
    """Updates shell by name

    Updates shell by name. # noqa: E501

    :param name: ID of shell to put
    :type name: str
    :param shell: Shell to be updated
    :type shell: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        shell = Shell.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_task(name, task):  # noqa: E501
    """Updates task by name

    Updates task by name. # noqa: E501

    :param name: ID of task to put
    :type name: str
    :param task: Task to be updated
    :type task: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        task = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
