from __future__ import annotations

from typing import List

from list_store import ListStore


class SimpleNameList(ListStore[str]):

    label: str = "item"

    def add_name(self, name: str) -> None:
        self.add(name)

    def names(self) -> List[str]:
        return self.all()


class FriendList(SimpleNameList):     label = "friend"


class CarGarage(SimpleNameList):      label = "car"


class PhotoAlbum(SimpleNameList):     label = "photo"


class Zoo(SimpleNameList):            label = "animal"


class GameInventory(SimpleNameList):  label = "item"


class Blog(SimpleNameList):           label = "post"


class Classroom(SimpleNameList):      label = "pupil"


class MusicBand(SimpleNameList):      label = "member"


class ShoppingList(SimpleNameList):   label = "product"


class LibraryShelf(SimpleNameList):   label = "book"


class TicketSystem(SimpleNameList):   label = "ticket"


class PetOwner(SimpleNameList):       label = "pet"


class StudyPlan(SimpleNameList):      label = "topic"


class Workshop(SimpleNameList):       label = "tool"


class CityTour(SimpleNameList):       label = "place"


class MoviePlaylist(SimpleNameList):  label = "movie"


class Conference(SimpleNameList):     label = "participant"


class DailyJournal(SimpleNameList):   label = "entry"


class WorkshopSchedule(SimpleNameList): label = "task"


class ProductCatalog(SimpleNameList): label = "product"


class TravelDestinations(SimpleNameList): label = "country"


class Bank(SimpleNameList):           label = "account"
