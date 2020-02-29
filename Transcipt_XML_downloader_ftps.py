
import ftplib
from ftplib import FTP_TLS
import os


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
        ftp = FTP_TLS()
        ftp.debugging = 2
        ftp.connect(self.ftp_server,990)
        print ftp
        ftp.login(self.ftp_user,self.ftp_pass)
        print(ftp)

if __name__ == "__main__":
     z = XMLDownloader(ftp_server='ftp server',ftp_user='ftp user',ftp_pass='ftp pass',download_path='download path',verbose=False)
    z.downloadXmlTranscripts()
