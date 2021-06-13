import urllib.parse
import dbus
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
import logging
import urllib

# create an instance of logger at a module level
logger = logging.getLogger(__name__)

variety = dbus.SessionBus().get_object("com.peterlevi.Variety", "/com/peterlevi/Variety").get_dbus_method(
    "process_command")


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        variety(event.get_data())


class VarietyExtension(Extension):

    def __init__(self):
        super(VarietyExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        description = "Type in your query and press Enter..."
        query = event.get_argument()
        actions = []


        possibleActions = {
            "next": ExtensionResultItem(
                icon="icons/variety.svg",
                name="Next",
                description="Next wallpaper",
                on_enter=ExtensionCustomAction(["--next"])
            ),
            "previous": ExtensionResultItem(
                icon="icons/variety.svg",
                name="Previous",
                description="Previous wallpaper",
                on_enter=ExtensionCustomAction(["--previous"])
            ),
            "favourite":
            ExtensionResultItem(
                icon="icons/variety.svg",
                name="Favourite",
                description="Move current wallpaper to Trash",
                on_enter=ExtensionCustomAction(["--favorite"])
            ),
            "trash": ExtensionResultItem(
                icon="icons/variety.svg",
                name="trash",
                description="Move current wallpaper to Trash",
                on_enter=ExtensionCustomAction(["--trash"])
            ),
            "history": ExtensionResultItem(
                icon="icons/variety.svg",
                name="History",
                description="Toggle History display",
                on_enter=ExtensionCustomAction(["--history"])
            ),
            "downloads": ExtensionResultItem(
                icon="icons/variety.svg",
                name="Downloads",
                description="Move current wallpaper to Trash",
                on_enter=ExtensionCustomAction(["--downloads"])
            ),
            "selector": ExtensionResultItem(
                icon="icons/variety.svg",
                name="selector",
                description="Show manual wallpaper selector - the thumbnail bar filled with images from the active image sources",
                on_enter=ExtensionCustomAction(["--selector"])
            )
        }

        for k in possibleActions.keys():
            if query is None or query.lower() in k:
                actions.append(possibleActions[k])

        return RenderResultListAction(actions)


if __name__ == '__main__':
    VarietyExtension().run()
