import sys
from abc import abstractmethod
from enum import Enum
import asyncio


class Events(Enum):
    GAME_PHASE_UNTAP = 0
    GAME_PHASE_UPKEEP = 1
    GAME_PHASE_DRAW = 2
    GAME_PHASE_COMBAT_START = 3
    GAME_PHASE_COMBAT_DECLARE_ATTACKERS = 4
    GAME_PHASE_COMBAT_DAMAGE = 5
    GAME_PHASE_COMBAT_END = 6
    GAME_PHASE_END = 7
    GAME_PHASE_CLEANUP = 8
    GAME_TURN_NEXT = 9
    CARD_MODIFY_POWER = 10
    CARD_MODIFY_TOUGHNESS = 11
    CARD_MODIFY_ABILITIES = 12
    CARD_DISABLE_ATTACK_BLOCK = 13
    CARD_ENABLE_ATTACK_BLOCK = 14
    CARD_DRAW = 15
    CARD_DESTROY = 16
    CARD_REVIVE = 17
    CARD_TAP = 18
    CARD_DISCARD = 19
    CARD_UNTAP = 20
    DECK_SCRY = 21
    PLAYER_DEAL_DAMAGE = 22,
    PLAY_INSTANTS = 23,
    GAME_END_PHASE = 24,
    GAME_WON = 25


class Event:

    type = None
    data = None

    def __init__(self, event_type, data = None):
        self.type = event_type
        self.data = data

    def __str__(self):
        return str(Events(self.type).name)

    def __int__(self):
        if isinstance(Events(self.type).value, tuple):
            return Events(self.type).value[0]

        return int(Events(self.type).value)



class EventObserver:
    def __init__(self):
        self.events = []

    def __call__(self, event_type, args):
        self.on_event(event_type, *args)

    @abstractmethod
    def on_event(self, event_type, *args):
        pass


class EventEmitter:
    def __init__(self):
        self.listeners = {}
        self.tasks = set()

    def on(self, event: Events, listener: callable):
        if event.value not in self.listeners:
            self.listeners[event.value] = []
        print("Adding listener", listener, "to event", event.value)
        self.listeners[event.value].append(listener)

    def off(self, event: Events, listener: callable):
        if event.value in self.listeners:
            self.listeners[event.value].remove(listener)
        print("Removing listener", listener, "from event", event.value)

    async def emit(self, event: Event):
        if event is None:
            print("Event is None")
        event_type = int(event)
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                async with asyncio.TaskGroup() as tg:
                    print("Calling listener", listener, "for event", event.type)
                    task = tg.create_task(listener(event.data))
                    self.tasks.add(task)
                    task.add_done_callback(self.tasks.discard)

    def cancel_all(self):
        for task in self.tasks:
            task.cancel()
        self.tasks.clear()

