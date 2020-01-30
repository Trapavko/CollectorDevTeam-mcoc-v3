from redbot.core import commands
import pygsheets
# from redbot.core import Config
# from .common.pages_menu import PagesMenu as Menu
#
# GOOGLECREDENTIALS = ''
#
class GSHandler(commands.Cog):
    # def __init__(self):
        # self.config = Config.get_conf(self, identifier=gshandler2019)


    @commands.command()
    async def testapi(self, ctx):
        """Test Command String"""
        collectordevteam = await ctx.bot.get_shared_api_tokens("collectordevteam")
        await ctx.send("Token: {}".format(collectordevteam))
        try:
            authentication = pygsheets.authorize(custom_credentials=collectordevteam)
            await ctx.send(authentication)
            # return pygsheets.authorize(custom_credentials=collectordevteam)
        except FileNotFoundError:
            err_msg = 'API token failed to authenticate'
            await ctx.send(err_msg)
            raise FileNotFoundError(err_msg)
