""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 6.1.0
"""

from discord.ext import commands
import discord
from discord.ext.commands import Context
import alpaca_communicator
from dotenv import load_dotenv
import os



# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot) -> None:
        self.bot = bot
        load_dotenv()

        self.PUBKEY = os.getenv("PUBKEY")
        self.SECKEY = os.getenv("SECKEY")
        self.BASEURL = os.getenv("BASEURL")
        self.POLYAPIKEY = os.getenv("POLYAPIKEY")
        self.alpaca = alpaca_communicator.AlpacaCommunicator(self.PUBKEY, self.SECKEY, self.BASEURL)


    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="market_buy",
        description="Buy individual shares of a stock",
    )
    async def market_buy(self, interaction: discord.Interaction, ticker: str, amount: int = 1) -> None:
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """ 
        alpaca = self.alpaca

        print(f"Context: {interaction}")
        print(f"Ticker: {ticker}")
        print(f"Amount: {amount}")
        alpaca.market_buy(ticker, amount)
        embed = discord.Embed(
            title="Market Buy",
            description=f"{interaction.user.id} bought {amount} shares of {ticker} at ${alpaca.get_stock_price({ticker})} a share",
            color=0xBEBEFE,
        )

        # Don't forget to remove "pass", I added this just because there's no content in the method.
        await interaction.response.send_message(embed=embed)

    @commands.hybrid_command(
        name="limit_buy",
        description="Buy x dollars of stock",
    )
    async def limit_buy(self, context: Context, ticker: str, limit_cost: int) -> None:
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """ 
        alpaca = self.alpaca

        print(f"Context: {context}")
        print(f"Ticker: {ticker}")
        print(f"limit_cost: {limit_cost}")
        alpaca.submit_order(ticker, "buy", limit_cost)
        # Do your stuff here

        # Don't forget to remove "pass", I added this just because there's no content in the method.
        pass
    
    @commands.hybrid_command(
        name="get_price",
        description="gets the last price of a stock",
    )
    async def test(self, context: Context, ticker: str) -> None:
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """ 
        alpaca = self.alpaca
        last_price = 0

        try: 
            last_price = alpaca.get_stock_price(ticker)
        except:
            pass
        # Do your stuff here

        # Don't forget to remove "pass", I added this just because there's no content in the method.
        pass


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(Template(bot))
