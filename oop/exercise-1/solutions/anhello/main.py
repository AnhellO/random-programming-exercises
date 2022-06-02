from __future__ import annotations

import random
import string

class Track:
    def __init__(self, **kwargs: dict) -> None:
        self._name = kwargs.get('name')
        self._is_starred = kwargs.get('starred', False)
        self._duration = kwargs.get('duration', 0.0)
        self._artist = kwargs.get('artist', 'Unknown')
        self._format = kwargs.get('format', 'mp3')
        self._reviews = []

    def __str__(self) -> str:
        return f"Name: {self._name}\nArtist: {self._artist}\nStarred: {self._is_starred}\nDuration: {self._duration}\nFormat: {self._format}\nReviews: {self._reviews}".strip()
    
    def display_letter(self, size: int=1000, chars: str=string.ascii_letters + ' ') -> str:
        return ''.join(random.choice(chars) for _ in range(size))
    
    def add_review(self, review: str) -> Track:
        self._reviews.append(review)
        return self
    
    def top_reviews(self) -> list:
        return [review for review in self._reviews if review == 5 * '*']

class MusicPlayer:
    def __init__(self, **kwargs: dict) -> None:
        self._brand = kwargs.get('brand')
        self._model = kwargs.get('model')
        self._formats = kwargs.get('formats', ['mp3', 'wav', 'flac'])
        self._tracks = []
    
    def __str__(self) -> str:
        return f"Brand: {self._brand}\Model: {self._model}\nFormats: {self._formats}\nTracks: {self._tracks}"
    
    def add_track(self, track: Track) -> MusicPlayer:
        self._tracks.append(track)
        return self
    
    def starred_tracks(self) -> str:
        return '\n'.join([str(track) for track in self._tracks if track._is_starred])
    
    def sorted_tracks(self) -> list:
        return [f"{item._name} - {item._duration}" for item in sorted(self._tracks, key=lambda track: track._duration)]

def main():
    # Testing a single track
    track = Track(name='Time Lapse', artist='Kalax', duration=4.20, starred=True)
    print(f"##### Track\n{track}\n")
    print(f"##### Letter\n{track.display_letter()}\n")
    
    track.add_review('****')
    track.add_review(5 * '*')
    track.add_review(2 * '*')
    track.add_review(5 * '*')
    print(f"##### Track\n{track}\n")
    print(f"##### Top Reviews: {track.top_reviews()}\n")
    
    # Testing the music player
    player = MusicPlayer(brand='SONY', model='XYZ123')
    player.add_track(track)
    player.add_track(Track(name='Vampires', artist='The Midnight', duration=5.17, starred=True))
    player.add_track(Track(name='Los Angeles', artist='The Midnight', duration=6.29, starred=False))
    player.add_track(Track(name='Tech Noir', artist='Gunship', duration=4.57, starred=True))
    player.add_track(Track(name='After Hours Run', artist='Mitch Murder', duration=3.40, starred=False))
    
    print(f"##### Starred Tracks\n{player.starred_tracks()}\n")
    print(f"##### Sorted Tracks\n{player.sorted_tracks()}\n")
    

if __name__ == "__main__":
    main()