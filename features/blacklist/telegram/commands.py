from aiogram.types import Message
from aiogram import Router
from features.blacklist.domain.services import BlacklistService

def register_commands(router: Router, blacklist_service: BlacklistService):
    @router.message(lambda message: message.text.startswith("/start") or message.text.startswith("/help"))
    async def send_welcome(message: Message):
        await message.answer("""Hi! I'm your Blacklist Bot.
        - Use /list to view all blacklisted users.
        - Use /remove <user_id> to remove a user from the blacklist.""")

    @router.message(lambda message: message.text.startswith("/list"))
    async def list_blacklisted_users(message: Message):
        users = blacklist_service.get_all_users()
        if not users:
            await message.answer("No users in the blacklist.")
            return

        response = "\n".join([
            f"ID: {i+1}, {u.first_name} {u.last_name}, Phones: {u.phone_numbers}, Emails: {u.emails}, Telegrams: {u.telegrams}, Comment: {u.comment}"
            for i, u in enumerate(users)
        ])
        await message.answer(response)

    @router.message(lambda message: message.text.startswith("/remove"))
    async def remove_user_from_blacklist(message: Message):
        try:
            user_id = int(message.text.split(maxsplit=1)[1])
            blacklist_service.remove_user(user_id)
            await message.answer("User removed from blacklist.")
        except Exception as e:
            await message.answer(f"Error removing user: {e}")
