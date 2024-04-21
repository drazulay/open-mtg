from enum import Enum
import asyncio


class EventType(Enum):
    E_PHASE_UNTAP = 0
    E_PHASE_UPKEEP = 1
    E_PHASE_DRAW = 2
    E_PHASE_COMBAT_START = 3
    E_PHASE_COMBAT_DECLARE_ATTACKERS = 4
    E_PHASE_COMBAT_DAMAGE = 5
    E_PHASE_COMBAT_END = 6
    E_PHASE_END = 7
    E_PHASE_CLEANUP = 8
    E_START_NEXT_TURN = 9
    E_START_NEXT_PHASE = 10
    E_MOD_PLAYER_HEALTH = 11
    E_MOD_CARD_HEALTH = 12
    E_PROCESS_ABILITIES = 13
    E_GAME_WON = 14
    E_GAME_START = 15
    E_GAME_STOP = 16
    E_DECK_EDIT = 17
    E_CONFIG_EDIT = 18
    E_CARD_FROM_HAND_TO_TABLE = 19
    E_CARD_FROM_TABLE_TO_HAND = 20
    E_CARD_FROM_HAND_TO_GRAVEYARD = 21
    E_CARD_FROM_TABLE_TO_GRAVEYARD = 22
    E_CARD_FROM_GRAVEYARD_TO_HAND = 23
    E_CARD_FROM_GRAVEYARD_TO_TABLE = 24
    E_CARD_FROM_STACK_TO_HAND = 25


class Event:
    def __init__(self, event_type: EventType, data=None):
        self.event_type = event_type
        self.data = data

    def __str__(self):
        return f'{self.event_type} {hash(self)}'

    def __repr__(self):
        return f'{self.event_type} {hash(self)}'

    def __hash__(self):
        return hash(self.event_type)

    def __eq__(self, other):
        return self.event_type == other.event_type

    def __ne__(self, other):
        return self.event_type != other.event_type

    def type(self):
        return self.event_type

    def data(self):
        return self.data

    def callback(self):
        return self.callback

    def cancel(self):
        self.callback.cancel()

    def __del__(self):
        self.cancel()


class EventEmitter():
    def __init__(self):
        self.events = {}

    def on(self, event, callback):
        if event not in self.events:
            self.events[event] = set()
        self.events[event].add(callback)

    def off(self, event, callback):
        if event in self.events:
            self.events[event].remove(callback)

    def cancel_all(self):
        for event_type in self.events:
            for event in self.events[event_type]:
                self.events[event_type].get(event).cancel()

    def emit(self, event: Event):
        if event.event_type in self.events:
            for callback in self.events[event.event_type]:
                callback(event)
