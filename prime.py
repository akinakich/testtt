from imports import *


logging.basicConfig(level= logging.INFO)

#storage = MemoryStorage()
bot = Bot(config.token)
dp = dp = Dispatcher(storage=MemoryStorage())

async def on_startup(_):
	print('Я запустился!')


class UserState(StatesGroup):
	menu1 = State()
	toplivocount = State()
	sumtoplivo = State()
	menu = State()
	test= State()
	remont = State()
	sumremont = State()
	pismo = State()
	sumshtraf = State()
	perehod = State()
	komandirdays = State()
	zp = State()
	nezamer = State()
	moika = State()
	moikatwo = State()
	platdoroga = State()
	platon = State()
	prochee = State()
	math = State()


i=0


countdaysk = ''


sum_toplivo = ''

zarplata = 0
procheeraz = 0



remontdays = 0
sumremont = 0
doroga = 0
mechanik = 1000



@dp.message(Command(commands=["start"]))
async def command_start_handler(message: types.Message, state: FSMContext):
	await message.answer('Привет! Я создан чтобы облегчить работу предприятию "Прайм - Групп и Ко"!',reply_markup=kb.get_menu1())

	await state.set_state(UserState.menu1)
	
	@dp.callback_query(state=UserState.menu1)
	async def stoptopupcall(callback_query: types.CallbackQuery, state: FSMContext):
		if callback_query.data=='ras':
			await callback_query.message.answer('Введите сколько рублей принесла машина грязными: ')
			await callback_query.answer()
			await state.set_state(UserState.perehod)
		elif callback_query.data=='dvas':
			await message.answer('Тогда я отдыхать!')


	@dp.message(state=UserState.perehod)
	async def command_start_handler(message: types.Message, state: FSMContext):
		dohodg = ''
		await state.update_data(dohodg = message.text.replace(',', '.').replace(' ', ''))
		print(dohodg)
		await message.answer('Выберите какую машину хотите рассчитать:', reply_markup=kb.get_menu())
		await state.set_state(UserState.menu)


	@dp.callback_query(state=UserState.menu)
	async def stoptopupcall(callback_query: types.CallbackQuery, state: FSMContext):
		await state.update_data(car = callback_query.data)
		print(callback_query.data)
		await bot.send_message(chat_id = callback_query.from_user.id, text = 'Сколько раз вы заправлялись: ')
		await state.set_state(UserState.toplivocount)
		await callback_query.answer()
		

	@dp.message(state=UserState.toplivocount)
	async def jobs_text(message: types.Message, state: FSMContext):
		global i
		count = ''
		await state.update_data(count = message.text)
		await message.answer('Введите сумму 1 заправки:')
		i=1
		zapravki = []
		await state.update_data(zapravki = zapravki)
		await state.set_state(UserState.sumtoplivo)


	@dp.message(state=UserState.sumtoplivo)
	async def jobs_text(message: types.Message, state: FSMContext):
		global i
		zapravki = await state.get_data()
		zapravki = zapravki['zapravki']
		zapravki.append(message.text.replace(',', '.').replace(' ', ''))
		count = await state.get_data()
		if i!=int(count['count']):
			await message.answer(f'Введите сумму {i+1} заправки: ')
			await state.set_state(UserState.sumtoplivo)
			i=i+1
		else:
			print(zapravki)
			sums = 0.0
			for x in range(len(zapravki)):
				sums = sums + float(zapravki[x])
			i=0
			car = await state.get_data()
			car = car['car']
			await bot.send_message(chat_id = message.from_user.id, text = f'Сколько раз был произведен ремонт {car} машины: ')
			await state.update_data(sums=sums)
			await state.update_data(zapravki=zapravki)
			await state.set_state(UserState.remont)

	@dp.message(state=UserState.remont)
	async def remont_taker(message: types.Message, state: FSMContext):
		global i
		await state.update_data(countr = message.text)
		await message.answer('Введите сумму 1 ремонта + запчастей: ')
		i = 1
		remontik = []
		await state.update_data(remontik = remontik)
		await state.set_state(UserState.sumremont)

	@dp.message(state=UserState.sumremont)
	async def remont_taker(message: types.Message, state: FSMContext):
		global i
		remontik = await state.get_data()
		remontik = remontik['remontik']
		remontik.append(message.text.replace(',', '.').replace(' ', ''))
		countr = await state.get_data()
		countr = countr['countr']
		if i!=int(countr):
			await message.answer(f'Введите сумму {i+1} ремонта + запчастей: ')
			await state.set_state(UserState.sumremont)
			i=i+1
		else:
			print(remontik)
			sumsr = 0
			for x in range(len(remontik)):
				sumsr = sumsr + float(remontik[x])
			i = 0
			
			car = await state.get_data()
			print(car)
			car = car['car']
			await bot.send_message(chat_id = message.from_user.id, text = f'Сколько писем "счастья" поймала {car} машина: ')
			await state.update_data(sumsr=sumsr)
			await state.update_data(remontik=remontik)
			await state.set_state(UserState.pismo)

	@dp.message(state=UserState.pismo)
	async def shtraf_taker(message: types.Message, state: FSMContext):
		global i
		countshtraf = ''
		await state.update_data(countshtraf = message.text)
		await message.answer('Введите сумму 1 штрафа: ')
		i = 1
		shrafi = []
		await state.update_data(shrafi = shrafi)
		await state.set_state(UserState.sumshtraf)

	@dp.message(state=UserState.sumshtraf)
	async def shtraf_taker(message: types.Message, state: FSMContext):
		shrafi = await state.get_data()
		shrafi = shrafi['shrafi']
		shrafi.append(message.text.replace(',', '.').replace(' ', ''))
		global i
		countshtraf = await state.get_data()
		countshtraf = countshtraf['countshtraf']
		if i!=int(countshtraf):
			await message.answer(f'Введите сумму {i+1} штрафа: ')
			await state.set_state(UserState.sumshtraf)
			i=i+1
		else:
			print(shrafi)
			summashtravov = 0
			for x in range(len(shrafi)):
				summashtravov = summashtravov + float(shrafi[x])
			i = 0
			car = await state.get_data()
			print(car)
			car = car['car']
			await bot.send_message(chat_id = message.from_user.id, text = f'Сколько было командировочных дней у водителя машины {car}: ')
			await state.update_data(summashtravov=summashtravov)
			await state.update_data(shrafi = shrafi)
			await state.set_state(UserState.komandirdays)

	@dp.message(state=UserState.komandirdays)
	async def komandirdni(message: types.Message, state: FSMContext):
		car = await state.get_data()
		print(car)
		car = car['car']
		await state.update_data(countdays = message.text.replace(',', '.').replace(' ', ''))
		await bot.send_message(chat_id = message.from_user.id, text = f'Сколько километров проехал водитель на {car} машине: ')
		await state.set_state(UserState.zp)


	@dp.message(state=UserState.zp)
	async def zarplata_math(message: types.Message, state: FSMContext):
		km = 0
		car = await state.get_data()
		print(car)
		car = car['car']
		await state.update_data(km = message.text.replace(',', '.').replace(' ', ''))
		zarplata = 8*float(km)
		print(zarplata)
		await state.update_data(zarplata=zarplata)
		await bot.send_message(chat_id = message.from_user.id, text = f'Сколько штук незамерзайки было потрачено на машине {car}: ')
		await state.set_state(UserState.nezamer)


	@dp.message(state=UserState.nezamer)
	async def komandirdni(message: types.Message, state: FSMContext):
		car = await state.get_data()
		print(car)
		car = car['car']
		await state.update_data(nezamerkakolvo = message.text.replace(',', '.').replace(' ', ''))
		await bot.send_message(chat_id = message.from_user.id, text = f'Сколько раз машина {car} была на мойке: ')
		await state.set_state(UserState.moika)

	@dp.message(state=UserState.moika)
	async def moika_math(message: types.Message, state: FSMContext):
		global i
		countmoika = ''
		await state.update_data(countmoika = message.text)
		await message.answer('Введите кол-во рублей потраченных на 1 мойке: ')
		i = 1
		moiki = []
		await state.update_data(moiki = moiki)
		await state.set_state(UserState.moikatwo)

	@dp.message(state=UserState.moikatwo)
	async def moika_math(message: types.Message, state: FSMContext):
		global i
		moiki= await state.get_data()
		moiki = moiki['moiki']
		car = await state.get_data()
		print(car)
		car = car['car']
		countmoika = await state.get_data()
		countmoika = countmoika['countmoika']
		
		moiki.append(message.text.replace(',', '.').replace(' ', ''))
		if i!=int(countmoika):
			await message.answer(f'Введите кол-во рублей потраченных на {i+1} мойке: ')
			await state.set_state(UserState.moikatwo)
			i=i+1
		else:
			summamoiki = 0
			for x in range(len(moiki)):
				summamoiki = summamoiki + float(moiki[x])
			print(summamoiki)
			
			i = 0
			await bot.send_message(chat_id = message.from_user.id, text = f'Сколько было потрачено рублей за платную дорогу на машине {car} : ')
			await state.update_data(summamoiki=summamoiki) #
			await state.update_data(moiki=moiki)
			await state.set_state(UserState.platdoroga)

	@dp.message(state=UserState.platdoroga)
	async def doroga(message: types.Message, state: FSMContext):
		car = await state.get_data()
		print(car)
		car = car['car']
		potrachdoroga = 0
		await state.update_data(potrachdoroga = message.text.replace(',', '.').replace(' ', ''))
		print('Платная дорога: ', potrachdoroga)
		await bot.send_message(chat_id = message.from_user.id, text = f'Сколько было потрачено рублей за платон на машине {car} : ')
		await state.set_state(UserState.platon)

	@dp.message(state=UserState.platon)
	async def platonic(message: types.Message, state: FSMContext):
		car = await state.get_data()
		print(car)
		car = car['car']
		await state.update_data(platonsumm = message.text.replace(',', '.').replace(' ', ''))
		await bot.send_message(chat_id = message.from_user.id, text = f'Сколько было потрачено рублей на прочие расходы на машине {car} : ')
		await state.set_state(UserState.prochee)

	@dp.message(state=UserState.prochee)
	async def prochie(message: types.Message, state: FSMContext):
		await state.update_data(procheeraz = message.text.replace(',', '.').replace(' ', ''))





		medic = 834
		await state.update_data(medic = medic)
		info = await state.get_data()
		
		dohodg = info['dohodg']
		car = info['car']
		count = info['count']
		sums = info['sums']
		countr = info['countr']
		sumsr = info['sumsr']
		countshtraf = info['countshtraf']
		summashtravov = info['summashtravov']
		countdays = info['countdays']
		countmoika = info['countmoika']
		summamoiki = info['summamoiki']
		nezamerkakolvo = info['nezamerkakolvo']
		km = info['km']
		medic = info['medic']
		platonsumm = info['platonsumm']
		potrachdoroga = info['potrachdoroga']
		procheeraz = info['procheeraz']



		gps = 0
		if car == 'К080ВТ' or car == 'А507ВТ':
			gps = 550
		else:
			gps = 500

		
		pribil1 = float(sums) + float(sumsr) + float(summashtravov) + float(summamoiki) + int(medic) + int(mechanik) + float(platonsumm) + float(potrachdoroga) + int(gps) + float(procheeraz)
		pribil2 = (75 * float(nezamerkakolvo))
		pribil3 = (700 * float(countdays))
		pribil4 = (8 * float(km))
		pribil5 = pribil1 + pribil2 + pribil3 + pribil4
		pribil = float(dohodg) - pribil5
		otchet = f'''\n
			Выбранный автомобиль: {car}\n
			Грязный доход машины: {dohodg} рублей\n
			------------------------------------------------------------------------------
			Количество заправок: {count}\n
			Сумма заправок: {sums} рублей\n
			------------------------------------------------------------------------------
			Количество ремонтов: {countr}\n
			Сумма ремонтов: {sumsr} рублей\n
			------------------------------------------------------------------------------
			Количество штрафов: {countshtraf}\n
			Сумма штрафов: {summashtravov} рублей\n
			------------------------------------------------------------------------------
			Командировочных дней было: {countdays}\n
			Общая сумма возмещения командировочных расходов: {700*float(countdays)} рублей\n
			------------------------------------------------------------------------------
			Машина была на мойке: {countmoika} раз(а)\n
			Сумма потраченная на мойку: {summamoiki} рублей\n
			------------------------------------------------------------------------------
			Было куплено {nezamerkakolvo} незамерзайки\n
			Было потрачено на незамерзайку: {75 * float(nezamerkakolvo)} рублей\n
			------------------------------------------------------------------------------
			Водитель проехал {km} километров\n
			Зарплата водителю при учете 8 рублей/километр: {float(km)*8} рублей\n
			------------------------------------------------------------------------------
			Оплата медику: {medic} рублей\n
			Оплата механику: {mechanik} рублей\n
			------------------------------------------------------------------------------
			Общая сумма за платон: {platonsumm} рублей\n
			Общая сумма за платные дороги: {potrachdoroga} рублей\n
			------------------------------------------------------------------------------
			Общая сумма за GPS: {gps} рублей\n
			Общая сумма за прочие расходы: {procheeraz} рублей\n
			------------------------------------------------------------------------------
			------------------------------------------------------------------------------
			------------------------------------------------------------------------------
			Чистая прибыль машины {car} = {pribil} рублей.
			'''

		f = open('otchetic.txt', 'w')
		f.write(otchet)
		f.close()
		document = FSInputFile('otchetic.txt')
		await bot.send_message(chat_id = -1001896087530, text = f'Отчет за: {str(date.today())} ')
		await bot.send_document(-1001896087530, document)
		await state.clear()
		await message.answer('Отчёт сформирован\n\nПроизведем еще один рассчёт?',reply_markup=kb.get_menu1())
		await state.set_state(UserState.menu1)

























async def main():
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())
