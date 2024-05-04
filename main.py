import json
import asyncio
import logging

from utils import is_valid_iso, not_valid_data, not_valid_json
from config import valid_formats, dp, bot
from format_data import aggregate_salary_data


@dp.message()
async def read_input(message):
    try:
        data = json.loads(message.text)

        # if data.keys() == valid_formats.keys() and data["group_type"] == valid_formats["group_type"]:
        if data.keys() == valid_formats.keys():
            if is_valid_iso(data['dt_from']) and is_valid_iso(data['dt_upto']):
                await message.reply(aggregate_salary_data(data['dt_from'], data['dt_upto'], data['group_type']))
                return

        await message.reply(not_valid_json())

    except json.JSONDecodeError:
        await message.reply(not_valid_data())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
