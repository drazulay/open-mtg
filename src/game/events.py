import time
import threading
import queue

from enum import Enum

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
        return self.event_type == other

    def __ne__(self, other):
        return self.event_type != other

    def type(self):
        return self.event_type

    def data(self):
        return self.data


class EventEmitter():
    def __init__(self):
        self.work_queue = queue.Queue()
        self.events = {}

        self.tasks = [(f'EventConsumer-{i}', self.process) for i in range(4)]
        self.workers = []

    def start_workers(self):
        for name, target in self.tasks:
            print(f'Starting worker {name}')
            worker = threading.Thread(name=name, target=target,
                                      args=(name, self.work_queue))
            worker.start()
            self.workers.append(worker)

    def on(self, event, callback):
        if event not in self.events:
            self.events[event] = set()

        self.events[event].add(callback)

    def off(self, event, callback):
        if event in self.events:
            self.events[event].remove(callback)

    def join_all(self):
        for worker in self.workers:
            worker.join(0.1)

    def emit(self, event: EventType, data=None):
        print("Emitting event", event, "with data", data)

        callbacks = self.events.get(event)

        if callbacks is None:
            return

        for callback in callbacks:
            self.work_queue.put([event, callback, data])

    def process(self, name, queue):
        """
        :type queue: queue.Queue
        """
        while True:
            event_name, callback, data = self.work_queue.get()
            print(f'{name} is processing {event_name} with callback {callback}')
            callback(data)
