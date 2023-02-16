from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters import Text
from aiogram import types
from bs4 import BeautifulSoup
import requests
from aiogram.types import FSInputFile
import asyncio
from aiogram.types import URLInputFile
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from aiogram.methods.send_animation import SendAnimation
from aiogram.methods import SendAnimation
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging
import keyb as kb
import config
from aiogram.types import InputFile
from aiogram.methods.send_document import SendDocument
from datetime import date
from aiogram.fsm.storage.memory import MemoryStorage