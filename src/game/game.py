import asyncio
import sys

from src.game.state import State
from src.player.player import Player, Players
from src.game.event import Event, Events, EventEmitter


class Game:

    def __init__(self, event_emitter=None, state=None):
        self.state = State(
            event_emitter=event_emitter) if state is None else state
        self.event_emitter = event_emitter
        self.run = True

    async def end_run(self):
        self.event_emitter.cancel_all()
        self.run = False

    async def new_game(self):
        self.state.add_player(Player(Players.PLAYER))
        self.state.add_player(Player(Players.OPPONENT))
        print("Starting game")
        while self.run:
            self.event_emitter.on(Events.GAME_WON, self.end_run)
            await self.event_emitter.emit(Event(Events.GAME_TURN_NEXT, self.state.turn))


if __name__ == '__main__':
    event_emitter = EventEmitter()
    game = Game(event_emitter=event_emitter)


    async def test():
        try:
            await game.new_game()
        except Exception as e:
            print(e)

    try:
        asyncio.run(test())
    except KeyboardInterrupt:
        print("Exiting")
        exit(0)
