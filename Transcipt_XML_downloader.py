import pysftp
import os
from settings import *


class XMLDownloader(object):
    '''
    This class will maintain the downloading of the XML transcripts.
    This will compare each file on the FTP with what is in the active
    '''

    def __init__(self,ftp_server, ftp_user,ftp_pass, download_path, verbose):
        self.ftp_server=ftp_server
        self.ftp_user = ftp_user
        self.ftp_pass = ftp_pass
        self.download_path = download_path
        self.verbose = verbose

    def downloadXmlTranscripts(self):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys=None
        with pysftp.Connection(self.ftp_server,username=self.ftp_user,password=self.ftp_pass,cnopts=cnopts) as sftp:
            print('Server Connected')
            localDirListing = os.listdir(self.download_path)
            print(type(localDirListing))
            print ("Gathered files in {}").format(self.download_path)
            with sftp.cd('Inbox'):    #change directory to the inbox
                print("Comparing files on FTP to what is in {} and downloading any new files").format(self.download_path)
                for file in sftp.listdir():
                    if file not in localDirListing and sftp.isfile(file):
                        print ('Downloading: {}'.format(file))
                        os.chdir(self.download_path)
                        sftp.get(file, preserve_mtime=True)
                    else:
                        if self.verbose:
                            print ("Skipping {} - it already exists in {}").format(file, self.download_path)

if __name__ == "__main__":
    z = XMLDownloader(ftp_server='ftp server',ftp_user='ftp user',ftp_pass='ftp pass',download_path='download path',verbose=False)
    z.downloadXmlTranscripts()
