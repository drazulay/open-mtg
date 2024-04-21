import random
import sys
from enum import Enum
from src.player.player import Players
from event import Events, Event, EventEmitter, EventObserver


class Phases(Enum):
    GAME_PHASE_UNTAP = 0
    GAME_PHASE_UPKEEP = 1
    GAME_PHASE_DRAW = 2
    GAME_PHASE_COMBAT_START = 3
    GAME_PHASE_COMBAT_DECLARE_ATTACKERS = 4
    GAME_PHASE_COMBAT_DAMAGE = 5
    GAME_PHASE_COMBAT_END = 6
    GAME_PHASE_END = 7
    GAME_PHASE_CLEANUP = 8


class State:
    phase = None
    turn = Players.PLAYER
    players = {}
    damage = 0
    event_emitter: EventEmitter
    winner = None

    def __init__(self, event_emitter: EventEmitter = None):
        super().__init__()

        self.event_emitter = event_emitter

        self.event_emitter.on(Events.GAME_TURN_NEXT, self.next_turn)
        self.event_emitter.on(Events.GAME_END_PHASE, self.next_phase)
        self.event_emitter.on(Events.GAME_PHASE_UNTAP, self.game_phase_untap)
        self.event_emitter.on(Events.GAME_PHASE_UPKEEP, self.game_phase_upkeep)
        self.event_emitter.on(Events.GAME_PHASE_DRAW, self.game_phase_draw)
        self.event_emitter.on(Events.GAME_PHASE_COMBAT_START, self.game_phase_combat_start)
        self.event_emitter.on(Events.GAME_PHASE_COMBAT_DECLARE_ATTACKERS, self.game_phase_combat_declare_attackers)
        self.event_emitter.on(Events.GAME_PHASE_COMBAT_DAMAGE, self.game_phase_combat_damage)
        self.event_emitter.on(Events.GAME_PHASE_COMBAT_END, self.game_phase_combat_end)
        self.event_emitter.on(Events.GAME_PHASE_END, self.game_phase_end)
        self.event_emitter.on(Events.GAME_PHASE_CLEANUP, self.game_phase_cleanup)
        self.event_emitter.on(Events.PLAY_INSTANTS, self.play_instants)
        self.event_emitter.on(Events.PLAYER_DEAL_DAMAGE, self.deal_damage)

    async def game_phase_untap(self, *args):
        self.phase = Phases.GAME_PHASE_UPKEEP

        print(f'Untap phase: {self.turn}')
        await self.event_emitter.emit(Event(Events.GAME_PHASE_UPKEEP, None))

    async def play_instants(self, *args):
        player = args[0]
        print(f'Playing instants: {player.player_type}')

    async def game_phase_upkeep(self, *args):
        self.phase = Phases.GAME_PHASE_UPKEEP

        opponent = self.get_current_opponent()
        player = self.get_current_player()
        print(f'{str(opponent.player_type).capitalize()} health: {opponent.health}, '
              f'{str(player.player_type).capitalize()} health: {player.health}')

        print(f'Upkeep phase: {self.turn}')
        await self.event_emitter.emit(Event(Events.PLAY_INSTANTS, None))
        await self.event_emitter.emit(Event(Events.GAME_PHASE_DRAW, None))

    async def game_phase_draw(self, *args):
        self.phase = Phases.GAME_PHASE_DRAW

        print(f'Draw phase: {self.turn}')
        await self.event_emitter.emit(Event(Events.PLAY_INSTANTS, None))
        await self.event_emitter.emit(Event(Events.GAME_PHASE_COMBAT_START, None))

    async def game_phase_combat_start(self, *args):
        self.phase = Phases.GAME_PHASE_COMBAT_START

        print(f'Combat start phase: {self.turn}')
        await self.event_emitter.emit(Event(Events.PLAY_INSTANTS, None))
        await self.event_emitter.emit(Event(Events.GAME_PHASE_COMBAT_DECLARE_ATTACKERS, None))

    async def game_phase_combat_declare_attackers(self, *args):
        self.phase = Phases.GAME_PHASE_COMBAT_DECLARE_ATTACKERS

        print(f'Combat declare attackers phase: {self.turn}')
        print("Choose attackers and blockers")
        await self.event_emitter.emit(Event(Events.GAME_PHASE_COMBAT_DAMAGE, None))

    async def game_phase_combat_damage(self, *args):
        self.phase = Phases.GAME_PHASE_COMBAT_DAMAGE

        print(f'Combat damage phase: {self.turn}')
        print("Gathering damage")
        self.damage = random.Random().randint(1, 5)
        print(f'Dealing damage: {self.damage}')
        await self.deal_damage(self.damage)
        await self.event_emitter.emit(Event(Events.GAME_PHASE_COMBAT_END, None))

    async def game_phase_combat_end(self, *args):
        self.phase = Phases.GAME_PHASE_COMBAT_END

        print(f'Combat end phase: {self.turn}')
        await self.event_emitter.emit(Event(Events.PLAY_INSTANTS, None))
        await self.event_emitter.emit(Event(Events.GAME_PHASE_END, None))

    async def game_phase_end(self, *args):
        self.phase = Phases.GAME_PHASE_END

        print(f'End phase: {self.turn}')
        await self.event_emitter.emit(Event(Events.PLAY_INSTANTS, None))
        await self.event_emitter.emit(Event(Events.GAME_PHASE_CLEANUP, None))

    async def game_phase_cleanup(self, *args):
        self.phase = Phases.GAME_PHASE_CLEANUP

        print(f'Cleanup phase: {self.turn}')
        await self.event_emitter.emit(Event(Events.GAME_TURN_NEXT, None))

    async def next_phase(self, last_phase, *args):
        if last_phase == None:
            self.phase = Phases(0)
            await self.event_emitter.emit(Event(Events.GAME_PHASE_UPKEEP, None))
        else:
            self.phase = Phases((self.phase.value + 1) % 9)
        print(f'Next phase: {last_phase} -> {self.phase}')

    async def next_turn(self, last_turn, *args):
        self.turn = (Players.PLAYER if self.turn == Players.OPPONENT
                     else Players.OPPONENT)
        print(f'Next turn: {last_turn} -> {self.turn}')
        await self.event_emitter.emit(Event(Events.GAME_PHASE_UNTAP))

    async def deal_damage(self, damage, *args):
        opponent = self.get_current_opponent()
        player = self.get_current_player()
        opponent.health -= damage
        print(f'{str(opponent.player_type).capitalize()} was dealt {damage} '
              f'damage by {player.player_type}, health: {opponent.health}')
        if player.health <= 0:
            self.winner = opponent
        elif opponent.health <= 0:
            self.winner = player
        if self.winner is not None:
            print(f'{str(self.winner.player_type).capitalize()} has won the game')
            await self.event_emitter.emit(Event(Events.GAME_WON, [self.winner]))

    def get_winner(self):
        return self.winner if self.winner is not None else False

    def add_player(self, player):
        if len(self.players.keys()) < 2:
            print("Adding player: ", player.player_type)
            self.players[player.player_type] = player
        else:
            print("Cannot add more players")

    def get_player(self, player_type):
        player = self.players.get(player_type)
        return player

    def get_current_player(self):
        return self.get_player(self.turn)

    def get_current_opponent(self):
        return self.get_player(Players.PLAYER if self.turn == Players.OPPONENT
                               else Players.OPPONENT)

    def get_current_phase(self):
        return self.phase

    def get_current_turn(self):
        return self.turn