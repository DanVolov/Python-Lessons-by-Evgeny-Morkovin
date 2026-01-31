from javascript import require, On, AsyncTask
from time import sleep

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
pvp = require('mineflayer-pvp').plugin
GoalFollow = pathfinder.goals.GoalFollow


bot = mineflayer.createBot({
    'host': 'Voleriangov.aternos.me',
    'port': 24964,
    'username': 'pvpBot',
    'version': '1.16.5'
})

bot.loadPlugin(pathfinder.pathfinder)
bot.loadPlugin(pvp)

@On(bot, 'spawn')
def spawn(*args):
    mcData = require('minecraft-data')(bot.version)
    movements = pathfinder.Movements(bot, mcData)

    @On(bot, 'chat')
    def pvp_handler(this, user, message, *args):
        if user != bot.username:
            if 'Атака' in message:
                player = bot.players[user]
                target = player.entity

                if not player:
                    bot.chat("I can't see you.")
                    return

                bot.pathfinder.setMovements(movements)
                goal = GoalFollow(target, 1)
                bot.pathfinder.setGoal(goal, True)
                bot.pvp.attack(target)

            if 'Стоп' in message:
                bot.pvp.stop()