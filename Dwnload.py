from __future__ import print_function
import httplib2, os
import requests

from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser (parents=[tools.argparser]).parse_args ()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_id.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
# = r"C:\Users\lokesh\PycharmProjects\MyPy\Rem_cam"

cwd_dir_1 = os.getcwd ()
filepath = cwd_dir_1 + '/RemCam'


# = os.path.join (cwd_dir, '.credentials')

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser ('~')
    credential_dir = os.path.join (home_dir, '.credentials')
    if not os.path.exists (credential_dir):
        os.makedirs (credential_dir)
    credential_path = os.path.join (credential_dir,
                                    'drive-python-quickstart.json')

    store = Storage (credential_path)
    credentials = store.get ()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets (CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow (flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run (flow, store)
        print ('Storing credentials to ' + credential_path)
    return credentials


def goog_D_Dloader(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session ()

    response = session.get (URL, params={'id': id}, stream=True)
    token = get_confirm_token (response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get (URL, params=params, stream=True)

    save_response_content (response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items ():
        if key.startswith ('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open (destination, "wb") as f:
        for chunk in response.iter_content (CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write (chunk)
    '''with open(filepath, 'wb') as f:
        for chunk in response.iter_content (CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write (chunk)'''


def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 100 files.
    """
    credentials = get_credentials ()
    http = credentials.authorize (httplib2.Http ())
    service = discovery.build ('drive', 'v3', http=http)

    results = service.files ().list (
        pageSize=100, fields="nextPageToken, files(id, name)").execute ()
    items = results.get ('files', [])
    if not items:
        print ('No files found.')
    else:
        print ('Files:')
        for item in items:
            print ('{0} ({1})'.format (item['name'], item['id']))
            if item['name'].startswith ("Manual Job"):
                goog_D_Dloader (item['id'], item['name'])


if __name__ == '__main__':
    main ()
