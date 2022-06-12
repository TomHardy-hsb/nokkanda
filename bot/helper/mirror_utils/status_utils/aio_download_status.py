from .status import Status
from bot.helper.ext_utils.bot_utils import MirrorStatus, get_readable_file_size, get_readable_time
from bot import DOWNLOAD_DIR, LOGGER    


class AioDownloadStatus(Status):
    def __init__(self, obj, listener):
        self.uid = listener.uid
        self.listener = listener
        self.obj = obj
        self.message = listener.message
        self.source = listener.source
    
    def gid(self):
        return self.obj.gid

    def sourcemsg(self):
        return self.source

    def path(self):
        return f"{DOWNLOAD_DIR}{self.uid}"

    def name(self):
        return self.obj.name

    def processed_bytes(self):
        return self.obj.downloaded_chunk

    def size_raw(self):
        return self.obj.size

    def size_raw_progress(self):
        return self.obj.size

    def getListener(self):
        return self.listener

    def size(self):
        return get_readable_file_size(self.obj.size)

    def totalsize(self):
        return get_readable_file_size(self.obj.gdfoldersize) 

    def currentsize(self):
        return get_readable_file_size(self.obj.size)

    def status(self):
        return MirrorStatus.STATUS_DOWNLOADINGANDUPLOADING

    def progress_raw(self):
        try:
            return self.obj.downloaded_chunk / self.obj.size * 100
        except ZeroDivisionError:
            return 0

    def downloaded_bytes(self):
        return get_readable_file_size(self.obj.completed_bytes)                    

    def downloadingname(self):
        return self.obj.currentname          

    def progress(self):
        return f'{round(self.progress_raw())}%'

    def speed_raw(self):
        """
        :return: Upload speed in Bytes/Seconds
        """
        return self.obj.speed()

    def speed(self):
        return f'{get_readable_file_size(self.speed_raw())}ps'

    def download(self):
        return self    

    def eta(self):
        try:
            seconds = (self.obj.size - self.obj.downloaded_chunk) / self.speed_raw()
            return f'{get_readable_time(seconds)}'
        except ZeroDivisionError:
            return '-'
      
    def cancel_download(self):
        LOGGER.info(f'Cancelling download on user request')
        self.obj.cancel_download()

    def genid(self):
        return None  

    def isgdfolder(self):
        return None

    def completed(self):
        return None       

    def which_client(self):
        return "AIO"  

    def upload_path(self):
        return f'{DOWNLOAD_DIR}{self.uid}/{self.name()}'

    def seeds(self):
        return None

    def leechers(self):
        return None