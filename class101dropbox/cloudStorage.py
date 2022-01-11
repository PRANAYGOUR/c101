import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'NeEuBcdERM0AAAAAAAAAAQPiO9YLOAcMfa4Gwxtr7m_C3qfCtAgyrlrC-yn_A0mv'
    transferData = TransferData(access_token)

    file_from = 'C:/class101dropbox/test2.txt'
    file_to = '/c101MobApp/test2.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("the file has been moved!!")


    main()