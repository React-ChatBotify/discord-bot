"""
Embed module for sponsor interest ticket instructions and actions.

This module defines the embed used when a user expresses interest in
becoming a sponsor. It provides sponsor information, and confirms
successful ticket creation in the appropriate channel.
"""

import discord

from bot.ui.buttons.common.close_ticket import close_ticket_btn
from bot.ui.buttons.common.export_ticket import export_ticket_btn
from bot.ui.embeds.embeds_manager import EmbedsManager
from bot.utils.console_logger import console_logger


class BecomeSponsorInfoEmbed:
    """
    Embed handler for sponsor interest tickets and interactions.
    """

    @staticmethod
    async def send(
        ctx_or_interaction,
        channel: discord.TextChannel,
        ticket_number: int,
    ) -> bool:
        """
        Send sponsor interest instructions and ticket confirmation.

        Args:
            ctx_or_interaction: The command context or interaction that triggered the embed.
            channel (discord.TextChannel): The channel to post the embed in.
            ticket_number (int): The assigned ticket number.

        Returns:
            bool: True if the embed was sent successfully, False otherwise.

        """
        try:
            await EmbedsManager.send_embed(
                ctx_or_interaction,
                channel=channel,
                title="📕 Become a Sponsor",
                description=(
                    "Interested to sponsor the project? Check out the link here: https://gallery.react-chatbotify.com/sponsors\n\n"
                    "📌 **Note:** Tickets will be addressed as soon as possible.\n"
                    "You will typically get a **first response within 24 hours**, "
                    "but resolution time may vary. Thank you for your understanding!"
                ),
                color=discord.Color.blue().value,
                footer_text=f"Ticket #{ticket_number}",
                buttons=[close_ticket_btn, export_ticket_btn],
            )

            await EmbedsManager.send_embed(
                ctx_or_interaction,
                title="Ticket Created",
                description=f"✅ Sponsor ticket created: {channel.mention}",
                color=discord.Color.green().value,
                ephemeral=True,
            )

            return True

        except Exception as e:
            console_logger.error(f"❌ Error sending message to sponsor channel: {str(e)}")
            return False
