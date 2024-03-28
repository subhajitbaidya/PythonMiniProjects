import time
import logging



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MediaFile: 
    
    
    def __init__(self, media ,type):
        self.media = media
        self.type = type
    
    def __str__(self):
        return f'Playing{self.type} {self.type}......'
    
    
    def play(self):
        print(f'Playing current {self.type} ' + self.media)
        
    def pause(self):
        print(f'{self.type} paused')
    
    def rewind(self):
        print(f'Re-playing current {self.type}')


#! Single Inheritance
class AudioFile(MediaFile):
    
    
    def __init__(self, song_name):
        MediaFile.__init__(self, song_name, type = 'music')
    
    
    @classmethod
    def music_file(cls, value):
        if value.endswith('.mp3'):
            return cls(value)
        else:
            print('Invalid input format')
            
    
    def play(self):
        return super().play()
    
    def pause(self):
        return super().pause()
    
    def rewind(self):
        return super().rewind()
    
    
#* Hybrid inheritance collectively with class AudioFile
class VideoFile(MediaFile):
    
    
    def __init__(self, video_name):
        MediaFile.__init__(self, video_name, type = 'movie')
    
    
    @classmethod
    def video_file(cls, value):
        if value.endswith('.mp4'):
            return cls(value)
        else:
            print('Invalid input format')
            
    
    def play(self):
        return super().play()
    
    def pause(self):
        return super().pause()
    
    def rewind(self):
        return super().rewind()
    
#& Multiple inheritance 
class PlayList(AudioFile, VideoFile, MediaFile):
    def __init__(self, song_name, *args):
        self.playlist = list(args)
        logging.info('Creating playlist')
        super().__init__(song_name)
        
    def make_playlist(self, *args):
        logging.info('Adding items to playlist')
        for item in args:
            self._add_to_playlist(item)
        return self.playlist
    
    def _add_to_playlist(self, item):
        if item.endswith('.mp3'):
            audio = AudioFile.music_file(item)
            self.playlist.append(audio)
        elif item.endswith('.mp4'):
            video = VideoFile.video_file(item)
            self.playlist.append(video)
        else:
            media = MediaFile(item, type="media")
            self.playlist.append(media)
            
    
    def play_playlist(self):
        logging.info('Playing playlist')
        for media in self.playlist:
            media.play()
            time.sleep(2) 
    
    
            
            
        
if __name__=='__main__':  
     
    
    
    logging.info('Running Media file')
    media = MediaFile('Image.gif', 'gif')  
    media.play()
    media.pause()
    media.rewind()  

    
    logging.info('Running Audio file')
    song = AudioFile('Audio.mp3')
    song.play()
    song.pause()
    song.rewind()

    logging.info('Running Video file')
    movie = VideoFile('Shibaji.mp4')
    movie.play()
    movie.pause()
    movie.rewind()

    logging.info('Running playlist')
    playlist = PlayList('Haale dil.mp3')
    playlist.make_playlist('Pani da.mp3', 'carry.mp4')
    playlist.play()
        
            
        

    playlist = PlayList('Trains.mp3')
    playlist.make_playlist('A smart Kid.mp3', 'Drapery Falls.mp4', 'Iron Maiden.jpg', 'Song list.pdf')
    playlist.play_playlist()







