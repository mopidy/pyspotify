from __future__ import unicode_literals

from spotify import ffi, lib
from spotify.utils import load


__all__ = [
    'Album',
]


class Album(object):
    """A Spotify album."""

    def __init__(self, sp_album):
        lib.sp_album_add_ref(sp_album)
        self.sp_album = ffi.gc(sp_album, lib.sp_album_release)

    @property
    def is_loaded(self):
        """Whether the album's data is loaded."""
        return bool(lib.sp_album_is_loaded(self.sp_album))

    def load(self, timeout=None):
        """Block until the album's data is loaded.

        :param timeout: seconds before giving up and raising an exception
        :type timeout: float
        :returns: self
        """
        return load(self, timeout=timeout)

    @property
    def link(self):
        """A :class:`Link` to the album."""
        from spotify.link import Link
        return Link(self)

    # TODO Add sp_album_* methods
